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
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib import auth

# Create your views here.

name = ""
def Get_name(request):
    global name;
    if request.user.is_authenticated():
        name = format(request.user.first_name)
    else:
        name = ""

active = {}

def make_active(act):
    global active
    active["home"] = "noactive"
    active["men"] = "noactive"
    active["women"] = "noactive"
    active["collections"] = "noactive"
    active["cart"] = "noactive"
    active[act] = "active"

def main_page(request):
    make_active("home")
    Get_name(request);
    #watches = Watches_Main.objects.all()
    watches = Watches_Main.objects.all().order_by('?')[:4]
    return render(request, 'store/kamstore.html', {'active':active, 'watches':watches, 'username':name})

def men_page(request):
    make_active("men")
    Get_name(request);
    watches = Watches_Men.objects.all().order_by('?')
    return render(request, 'store/Men.html', {'active':active, 'watches':watches, 'username':name})

def women_page(request):
    make_active("women")
    Get_name(request);
    watches = Watches_Women.objects.all().order_by('?')
    return render(request, 'store/Women.html', {'active':active, 'watches':watches, 'username':name})

def collections_page(request):
    make_active("collections")
    Get_name(request);
    watches = Collection_Model.objects.all()
    omegas = watches[0:4]
    zeniths = watches[4:]
    return render(request, 'store/Collections.html', {'active':active, 'omegas':omegas, 'zeniths':zeniths, 'username':name })

def cart(request):
    make_active("cart")
    Get_name(request);
    return render(request, 'store/Cart.html', {'username':name, 'active':active})

def add(request):
    return HttpResponse("Added")

def home(request):
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

def checkin(request):
    return render(request, 'store/checkin.html', {});

@login_required
def account_profile(request):
    if request.user.is_authenticated():
        args = {}
        args['name'] = format(request.user.first_name)
        args['surname'] = format(request.user.last_name)
        args['email'] = format(request.user.email)
        user = request.user
        return render(request, 'store/profile.html', {'args':args, 'username':args['name'], 'user':user});
    else:
        return render(request, 'store/checkin.html')
    """
    Show user greetings. ONly for logged in users.
    """
    #return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('/') 

@csrf_exempt
def paypal_success(request):
    """
    Tell user we got the payment.
    """
    return HttpResponse("Money is mine. Thanks.")


@login_required
def paypal_pay(request):
    paypal_dict = {
        "business": "andreyklimkin@yandex.ru",
        "amount": "100.00",
        "currency_code": "RUB",
        "item_name": "products in watches store",
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "success/",
        "cancel_return": "/cart/",
        "custom": str(request.user.id)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict}
    return render(request, "store/payment.html", context)