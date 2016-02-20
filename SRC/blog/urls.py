from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'^1/', 'blog.views.basic_one'),
    url(r'^2/', 'blog.views.template_two'),
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^admin/', include(admin.site.urls)),
]
