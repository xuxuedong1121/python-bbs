from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout,login,authenticate
import json
# Create your views here.
from bbs import models,comment_hander


Category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    artilce_list = models.Article.objects.filter(status='published')
    return render(request,'bbs/index.html',{'Category_list':Category_list,
                                            'artilce_list': artilce_list,
                                            'category_obj':category_obj,
                                            })

def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:
        artilce_list = models.Article.objects.filter(status='published')
    else:
        artilce_list = models.Article.objects.filter(category_id = category_obj.id,status='published')
    return render(request,'bbs/index.html',{'Category_list':Category_list,
                                            'category_obj':category_obj,
                                            'artilce_list':artilce_list,
                                            })
def acc_login(request):
    if  request.method == 'POST':
        print(request.POST)
        user = authenticate(username = request.POST.get('username'),
                            password = request.POST.get('password'))
        if user is not None:
            #pass authentcation
            login(request,user)
            # return HttpResponseRedirect('/bbs')
            return HttpResponseRedirect(request.GET.get('next')or'/bbs' )
        else:
            login_err = "Wrong username or password."
            return render(request,'login.html',{'loin_err':login_err})
    return  render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')


def article_detail(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    article_tree = comment_hander.bulid_tree(article_obj.comment_set.select_related())
    # print(article_obj)
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj,
                                                     'Category_list':Category_list,})


def comment(requset):
    print (requset.POST)
    if requset.method=='POST':
        new_comment_obj =models.Comment(
            article_id = requset.POST.get('article_id'),
            parent_comment_id = requset.POST.get('parent_comment_id') or None,
            comment_type = requset.POST.get('comment_typ'),
            user_id = requset.user.userprofile.id,
            comment = requset.POST.get('comment')
        )
        new_comment_obj.save()
        return HttpResponse('post-comment-success')

def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_hander.bulid_tree(article_obj.comment_set.select_related())
    tree_html = comment_hander.render_comment_tree(comment_tree)
    return HttpResponse(tree_html)

