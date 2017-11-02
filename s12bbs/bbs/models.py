#_*_coding:utf-8_*_
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class  Article(models.Model):
    tilte = models.CharField(max_length=255)
    brief = models.CharField(null=True,blank=True,max_length=255)
    category = models.ForeignKey("Category")
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile")
    pub_date = models.DateTimeField(blank=True,null=True)
    last_modify = models.DateTimeField(auto_now=True)
    priority  = models.IntegerField(u"优先级",default=1000)
    head_img = models.ImageField(u'文章标题图片',upload_to='uploads')
    status_choices = (('draft',u'草稿'),
                      ('published',u'已发布'),
                      ('hidden',u'隐藏'),
                      )
    status = models.CharField(choices=status_choices,default='published',max_length=32)
    def clean(self):
        if self.status == 'draft'and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a published.'))
        if self.status == 'published'and self.pub_date is None:
            self.pub_date = datetime.date.today()
    def __unicode__(self):
        return self.tilte

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u'所属文章')
    parent_comment = models.ForeignKey('self',related_name='my_children',blank=True,null=True)
    comment_choices = ((1,u'评论'),
                       (2,u'点赞'))
    comment_type = models.IntegerField(choices=comment_choices,default=1)
    user = models.ForeignKey("UserProfile")
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if self.comment_type == 1 and len(self.comment) ==  0:
            raise ValidationError(u'评论不能为空.')
    def __unicode__(self):
        return "%s,P:%s,%s"%(self.article,self.parent_comment,self.comment)

class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)
    brief = models.CharField(null=True,blank=True,max_length=255)
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField("UserProfile",blank=True)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255,blank=True,null=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)

    def __unicode__(self):
        return self.name





