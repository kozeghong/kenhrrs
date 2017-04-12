#-*- coding: utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# import json
from markdown import markdown
from cgi import escape

from .models import Article

def show(request, article_id=None):
    article = get_object_or_404(Article, pk=article_id, published=True)
    article.content = markdown(escape(article.content))
    return render(request, 'news/news-show.html', {'article': article})

def index(request):
    article_list = Article.objects.filter(published=True).order_by('-modify_time')
    return render(request, 'news/news-list.html', {'article_list': article_list})

@login_required
def board(request):
    article_list = Article.objects.all().order_by('-pk')
    return render(request, 'news/news-board.html', {'article_list': article_list})

@login_required
def createnew(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        summary = request.POST.get('summary', None)
        content = request.POST.get('content', None)
        
        if(title is None)or(summary is None)or(content is None):
            return render(request, 'news/news-createnew.html')

        if(title == "")or(summary == "")or(content == ""):
            return render(request, 'news/news-createnew.html')

        article = Article()
        article.title = title
        article.summary = summary
        article.content = content
        article.createdby = request.user
        article.modifiedby = request.user
        article.save()
        return redirect(reverse('news_board'))
    return render(request, 'news/news-createnew.html')

@login_required
def modify(request, article_id=None):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        new_title = request.POST.get('title', None)
        new_summary = request.POST.get('summary', None)
        new_content = request.POST.get('content', None)
        
        if(new_title is None)or(new_summary is None)or(new_content is None):
            return redirect(reverse('news_modify', args=(article_id,)))

        if(new_title == "")or(new_summary == "")or(new_content == ""):
            return redirect(reverse('news_modify', args=(article_id,)))

        article.title = new_title
        article.summary = new_summary
        article.content = new_content
        article.modifiedby = request.user
        article.save()
        return redirect(reverse('news_board'))
    return render(request, 'news/news-edit.html', {'article': article})

@login_required
def publish(request, article_id=None):
    article = get_object_or_404(Article, pk=article_id)
    article.published = not article.published
    # result = {'article_id': article.pk, 'published': article.published}
    article.save()
    # return HttpResponse(json.dumps(result), content_type='application/json')
    return redirect(reverse('news_board'))