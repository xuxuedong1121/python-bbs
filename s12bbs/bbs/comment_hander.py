#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 14:55
# @Author  : xuxuedong
# @Site    : 
# @File    : comment_hander.py
# @Software: PyCharm
import os, sys

def add_node(tree_dic,comment):
    if comment.parent_comment is None:
        #代表我是顶层
        tree_dic[comment]={}
    else: #循环当前整个字典找上级评论
        for k,v in tree_dic.items():
            if k == comment.parent_comment:#找到顶级评论
                print("find parent")
                tree_dic[comment.parent_comment][comment]={}
            else: #进入下一层
                print("keep going deeper")
                add_node(v,comment)

        # tree_dic[comment.parent_comment][comment] ={}
def render_tree_node(tree_dic,margin_val):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='comment-node' style='margin-left:%spx'>" % margin_val + k.comment \
              + "<span style='margin-left:20px'>%s </span>" %k.date + "<span style='margin-left:20px'>%s</span>" %k.user.name +\
               "<span style='margin-left:20px' class='glyphicon glyphicon-comment add-comment aria-hidden='true'></span>" + "</div>"
        html += ele
        html += render_tree_node(v,margin_val+10)
    return html

def render_comment_tree(tree_dic):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='root-comment'>"+ k.comment + "<span style='margin-left:20px'>%s </span>" \
            %k.date + "<span style='margin-left:20px'>%s</span>" %k.user.name \
        + "<span style='margin-left:20px' class='glyphicon glyphicon-comment add-comment aria-hidden='true'></span>" + "</div>"
        html += ele
        html += render_tree_node(v,10)
    return html
def  bulid_tree(comment_set):
    # print(comment_set)
    tree_dic = {}
    for comment in comment_set:
        add_node(tree_dic,comment)
    # print(tree_dic)
    for k,v in tree_dic.items():
        print(k,v)
    return tree_dic
