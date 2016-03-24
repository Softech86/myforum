# coding: utf-8
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from block.models import Block
from django.contrib.auth.models import User
from models import Article

# Create your views here.
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id = block_id)
    articles = Article.objects.filter(block = block).order_by("-last_update_timestamp")
    return render_to_response("article_list.html", {"articles": articles, "myblock": block}, context_instance = RequestContext(request))

def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id = block_id)
    print request.method, 'hahaha'
    if request.method == 'GET':
        return render_to_response("article_create.html", {"myblock": block}, context_instance = RequestContext(request))
    else:
        print request.POST
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, u'标题和内容均不能为空')
            return render_to_response(
                    "article_create.html",
                    {"myblock": block, "title": title, "content": content}, 
                    context_instance = RequestContext(request))
        author = User.objects.all()[0] #TODO:
        new_article = Article(block = block, author = author, title = title, content = content)
        new_article.save()
        messages.add_message(request, messages.INFO, u'成功发布文章 %s .' % title)
        return redirect(reverse("article_list", args = [block_id]))

def article_detail(request, block_id, article_id):
    block_id = int(block_id)
    block = Block.objects.get(id = block_id)
    article_id = int(article_id)
    article = Article.objects.get(id = article_id)
    return render_to_response("article_detail.html", {"myblock": block, "article": article}, context_instance = RequestContext(request)) 
