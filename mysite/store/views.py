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
def main_page(request):
    if request.user.is_authenticated():
        name = format(request.user.first_name)

    else:
        name = ""
    #watches = Watches_Main.objects.all()
    watches = Watches_Main.objects.all().order_by('?')[:4]
    return render(request, 'store/kamstore.html', {'watches':watches, 'username':name})

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

def checkin(request):
    return render(request, 'store/checkin.html', {});



@login_required
def account_profile(request):
    """
    Show user greetings. ONly for logged in users.
    """
    args = {}
    args['name'] = format(request.user.first_name)
    args['surname'] = format(request.user.last_name)
    args['email'] = format(request.user.email)
    user = request.user
    #resp = HttpResponse('https://api.vk.com/method/'status_get'?'''user.id'''&access_token='''

    return render(request, 'store/profile.html', {'args':args, 'username':args['name'], 'user':user});
    #return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('http://localhost:8000') 

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
        "amount": "00.00",
        "currency_code": "RUB",
        "item_name": "products in watches store",
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://localhost:8000/payment/success/",
        "cancel_return": "http://localhost:8000/cart/",
        "custom": str(request.user.id)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict}
    return render(request, "store/payment.html", context)