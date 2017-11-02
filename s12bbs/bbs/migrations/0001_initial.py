# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-28 16:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilte', models.CharField(max_length=255)),
                ('brief', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=1000, verbose_name='\u4f18\u5148\u7ea7')),
                ('status', models.CharField(choices=[('draft', '\u8349\u7a3f'), ('published', '\u5df2\u53d1\u5e03'), ('hidden', '\u9690\u85cf')], default='published', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('brief', models.CharField(blank=True, max_length=255, null=True)),
                ('set_as_top_menu', models.BooleanField(default=False)),
                ('position_index', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.IntegerField(choices=[('1', '\u8bc4\u8bba'), ('2', '\u70b9\u8d5e')], default=1)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Article', verbose_name='\u6240\u5c5e\u6587\u7ae0')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_children', to='bbs.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('signature', models.CharField(blank=True, max_length=255, null=True)),
                ('head_img', models.ImageField(blank=True, height_field=150, null=True, upload_to=b'', width_field=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile'),
        ),
        migrations.AddField(
            model_name='category',
            name='admins',
            field=models.ManyToManyField(blank=True, to='bbs.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Category'),
        ),
    ]
