from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',views.homepage),
    url(r'^index',views.index),
    url(r'^about',views.about),
    url(r'^shop',views.shop),
    url(r'^contact',views.contact),
    url(r'^cart',views.cart),
    url(r'^checkout',views.checkout),
    url(r'^thankyou',views.thankyou),
]

urlpatterns += staticfiles_urlpatterns()