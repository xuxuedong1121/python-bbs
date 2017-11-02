#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 22:35
# @Author  : xuxuedong
# @Site    : 
# @File    : customer.py
# @Software: PyCharm
import os, sys

from django import template
from django.template.defaultfilters import stringfilter
from  django.utils.html import format_html
register = template.Library()

@register.filter
def truncate_url(img_url):
    # print(dir(img_url))
    # print(img_url.name,img_url.url)

    return "/".join(img_url.name.split("/")[1:])
    # return   img_url.split("/",maxsplit=1)[1:]

@register.simple_tag
def filter_comment(article_obj):
    query_set = article_obj.comment_set.select_related()
    comments={
        'comment_count':query_set.filter(comment_type=1).count(),
        'thumb_count':query_set.filter(comment_type=2).count(),
    }
    return comments