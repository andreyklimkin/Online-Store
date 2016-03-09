# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from django.shortcuts import render
from .models import Watches_Main
from .models import Watches_Men
from .models import Watches_Women
from .models import Collection_Model
from django.http import HttpResponse
import random
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# Create your views here.
def main_page(request):
    #watches = Watches_Main.objects.all()
    watches = Watches_Main.objects.all().order_by('?')[:4]
    return render(request, 'store/kamstore.html', {'watches':watches})

def men_page(request):
    watches = Watches_Men.objects.all().order_by('?')
    return render(request, 'store/Men.html', {'watches':watches})

def women_page(request):
    watches = Watches_Women.objects.all().order_by('?')
    return render(request, 'store/Women.html', {'watches':watches})

def collections_page(request):
    watches = Collection_Model.objects.all()
    omegas = watches[0:4]
    zeniths = watches[4:]
    return render(request, 'store/Collections.html', {'omegas':omegas, 'zeniths':zeniths })

def cart(request):
    return render(request, 'store/Cart.html', {})

def add(request):
    return HttpResponse("Added")

def home(request):
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")


@login_required
def account_profile(request):
    """
    Show user greetings. ONly for logged in users.
    """
    return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('http://127.0.0.1:8000') 