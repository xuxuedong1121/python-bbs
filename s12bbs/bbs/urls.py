#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 21:22
# @Author  : xuxuedong
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
import os, sys
from django.conf.urls import url,include

from bbs import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/(\d+)/$',views.category),
    url(r'^detail/(\d+)/$',views.article_detail,name='article_detail'),
    url(r'^comment/$',views.comment,name='post_comment'),
    url(r'^comment_list/(\d+)/$',views.get_comments,name='get_comments'),

]