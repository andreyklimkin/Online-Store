
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from . import views 
from django.conf.urls.static import static
from django.conf import settings
import social.apps.django_app.urls
import paypal.standard.ipn.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'Men/$', views.men_page, name='Men'),
    url(r'^Women/$', views.women_page, name='Women'),
    url(r'^register', views.checkin, name='checkin'),
    url(r'^Collections', views.collections_page, name='Women'),
    url(r'^$', views.main_page, name='main_page'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^add-to-cart/$', views.add, name='add'),
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^Cart/$', views.cart, name='cart'),
    url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/login/$', views.home, name='login'),
    url(r'^accounts/profile/$', views.account_profile, name='profile'),
    url(r'^payment/cart/$', views.paypal_pay, name='cart'),
    url(r'^payment/success/$', views.paypal_success, name='success'),
    url(r'^paypal/', include(paypal.standard.ipn.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
