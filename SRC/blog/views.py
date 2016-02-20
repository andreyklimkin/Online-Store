# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Post
from django.utils import timezone
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# Create your views here.
def basic_one(request):
	#view = 'basic_one'
	#html = "<html><body>This is %s view</body><html>" % view
	#return HttpResponse(html)
	#name = ANDREI
    return render(request, 'blog/test.html', {})

def template_two(request):
	#view = 'basic_one'
	#html = "<html><body>This is %s view</body><html>" % view
	#return HttpResponse(html)
	view = "template_two"
	t = get_template('new.html');
	html = t.render(Context({'name': view}))
	return HttpResponse(html)
    #return render(request, 'blog/test.html', {})