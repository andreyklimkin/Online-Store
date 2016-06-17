# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from django.shortcuts import render
from .models import Collection_Model
from .models import Watches
from .models import Brands
from .models import Collections
from .models import Carts
from .models import Cart_Items
from .models import Purchases
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
from django.db.models import Q
import datetime

# Create your views here.

name = ""
def Get_name(request):
    global name;
    if request.user.is_authenticated():
        name = format(request.user.first_name)
    else:
        name = ""


active = {}

purchase_dict = {}

def make_active(act):
    global active
    active["home"] = "noactive"
    active["men"] = "noactive"
    active["women"] = "noactive"
    active["collections"] = "noactive"
    active["profile"] = "noactive"
    active["cart"] = "noactive"
    active[act] = "active"

def main_page(request):
    make_active("home")
    Get_name(request);
    #watches = Watches_Main.objects.all()
    watches = Watches.objects.all().order_by('-rating')[:4]
    return render(request, 'store/kamstore.html', {'active':active, 'watches':watches, 'username':name})

def men_page(request):
    make_active("men")
    Get_name(request);
    watches = Watches.objects.filter(gender="M").order_by('-rating')[:8]
    #watches = {}
    return render(request, 'store/Men.html', {'active':active, 'watches':watches, 'username':name})

def women_page(request):
    make_active("women")
    Get_name(request);
    watches = Watches.objects.filter(gender="F").order_by('-rating')[:8]
    return render(request, 'store/Women.html', {'active':active, 'watches':watches, 'username':name})

def collections_page(request):
    make_active("collections")
    Get_name(request);
    brands = Brands.objects.all()
    collections = Collections.objects.all()
    watches = Watches.objects.all()
    allbrands = brands
    allcollections = collections
    return render(request, 'store/Collections.html', {'active':active, 'brands':brands, 'collections': collections, \
                                                       'watches':watches, 'username':name, 'allbrands':allbrands, 'allcollections': allcollections})

def cart(request):
    make_active("cart")
    Get_name(request);
    if request.user.is_authenticated():
        user=request.user
        user_cart=Carts.objects.get(user_name=user)
        cart_items=Cart_Items.objects.filter(cart=user_cart)
        return render(request, 'store/Cart.html', {'username':name, 'active':active, 'cart_items':cart_items})
    else:
        return redirect('/register');

def add(request):
    #JSONdata = request.POST['data']
    #dict = simplejson.JSONDecoder().decode( JSONdata )
    if request.user.is_authenticated():
        item_name = request.GET['item']
        item = Watches.objects.get(model=item_name)
        user=request.user
        user_cart=Carts.objects.get(user_name=user)
        cnt = Cart_Items.objects.filter(cart=user_cart, item=item).count()
        if(cnt > 0):
            return HttpResponse("IsIn");
        else:
            new = Cart_Items(cart=user_cart, item=item)
            new.save()
        return HttpResponse("Added")
    else:
        return HttpResponse("NR");

def delete(request):
    #JSONdata = request.POST['data']
    #dict = simplejson.JSONDecoder().decode( JSONdata )
    #return HttpResponse("Deleted")
    if request.user.is_authenticated():
        item_name = request.GET['item']
        item = Watches.objects.get(model=item_name)
        user=request.user
        user_cart=Carts.objects.get(user_name=user)
        Cart_Items.objects.filter(cart=user_cart, item=item).delete()
        cart_items=Cart_Items.objects.filter(cart=user_cart)
        #return render(request, 'store/Cart.html', {'username':name, 'active':active, 'cart_items':cart_items})
        return HttpResponse("OK")
    else:
        return render(request, 'store/checkin.html', {});

def order_collections(request):
    brand=request.GET['brand']
    collection=request.GET['collection']
    make_active("collections")
    Get_name(request)
    brands = Brands.objects.filter(name=brand)
    collections = Collections.objects.filter(name=collection)
    watches = Watches.objects.all()
    allcollections = Collections.objects.filter()
    allbrands = Brands.objects.all()
    return render(request, 'store/Collections.html', {'active':active, 'brands':brands, 'collections': collections, \
                                                       'watches':watches, 'username':name, 'allbrands':allbrands, 'allcollections': allcollections})

def home(request):
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

def checkin(request):
    return render(request, 'store/checkin.html', {});

def search(request):
    search_str = request.GET['str'].lower()

    make_active("")
    Get_name(request);
    watches = []
    for s in search_str.split():
        watches += Watches.objects.filter(Q(model__contains=s)| Q(collection__name__contains=s) | Q(collection__brand__name__contains=s))
    #watches2 = Watches.objects.filter(collection__contains=s)
    #watches1.update(watches2)
    #watches = {}
    return render(request, 'store/search.html', {'active':active, 'watches':watches, 'username':name})

@login_required
def account_profile(request):
    make_active("profile")
    user=request.user
    if(Carts.objects.filter(user_name=user).count() == 0):
        new = Carts(user_name=user)
        new.save()
    args = {}
    args['name'] = format(request.user.first_name)
    args['surname'] = format(request.user.last_name)
    args['email'] = format(request.user.email)
    user = request.user
    return render(request, 'store/profile.html', {'args':args, 'active':active, 'username':args['name'], 'user':user});
    """
    Show user greetings. ONly for logged in users.
    """
    #return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


@login_required
def account_purchases(request):
    user=request.user
    args = {}
    args['name'] = format(request.user.first_name)
    args['surname'] = format(request.user.last_name)
    args['email'] = format(request.user.email)
    make_active("profile")
    purchases=Purchases.objects.filter(user_name=user)
    return render(request, 'store/purchases.html', {'args':args, 'active':active, 'username':args['name'], 'user':user, 'watches':purchases})
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


@login_required
def paypal_pay(request):
    global purchase_dict
    total_price = request.GET['total_price']
    user=request.user
    strs = request.GET['item_price'].split("$")
    #f = open('test.txt', 'w')
        #print(strs, file=g)
    purchase_dict[user] = {}
    for i in range(0, len(strs) - 1, 2):
        purchase_dict[user][strs[i]] = float(strs[i + 1])
    #for s in purchases[user]:
        #f.write(str(purchases[user]))
    user_cart=Carts.objects.get(user_name=user)
    cart_items=Cart_Items.objects.filter(cart=user_cart)
    purchases = ""
    for a in cart_items:
        purchases += str(a.item.model) + "\n";
    paypal_dict = {
        "business": request.user.email,
        "amount": total_price,
        "currency_code": "USD",
        "item_name": purchases,
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "success/",
        "cancel_return": "/cart/",
        "custom": str(request.user)
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict}
    #sreturn HttpResponse(purchases)
    return render(request, "store/payment.html", context)

@login_required
def test(request):
    user = request.user
    user_cart=Carts.objects.get(user_name=user)
    cart_items=Cart_Items.objects.filter(cart=user_cart)
    for it in cart_items:
        #Cart_Items.objects.filter(cart=user_cart, item=it.item).delete()
        if(Purchases.objects.filter(user_name=user, item=it.item).count() == 0):
            new = Purchases(user_name=user, item=it.item)
            new.save()
    for it in cart_items:
        Cart_Items.objects.filter(cart=user_cart, item=it.item).delete()
    #purchases=Purchases.objects.filter(user_name=user)
    #new = Carts(user_name=user)
    #new.save()

    """
    Tell user we got the payment.
    """
    thanks = "Thank you for the purchase"
    return redirect('/accounts/purchases')
    #return redirect('/accounts/profile')
    #return render(request, 'store/profile.html', {'user':user, 'active':active, 'mess':thanks})
    #return render(request, 'store/purchases.html', {'user':user, 'active':active, 'watches':purchases})

@csrf_exempt
def paypal_success(request):
    user = request.user
    user_cart=Carts.objects.get(user_name=user)
    cart_items=Cart_Items.objects.filter(cart=user_cart)
    for it in cart_items:
        #Cart_Items.objects.filter(cart=user_cart, item=it.item).delete()
        if(Purchases.objects.filter(user_name=user, item=it.item).count() == 0):
            new = Purchases(user_name=user, item=it.item)
            new.save()
    for it in cart_items:
        Cart_Items.objects.filter(cart=user_cart, item=it.item).delete()
    #purchases=Purchases.objects.filter(user_name=user)
    #new = Carts(user_name=user)
    #new.save()

    """
    Tell user we got the payment.
    """
    thanks = "Thank you for the purchase"
    return redirect('/accounts/purchases')
