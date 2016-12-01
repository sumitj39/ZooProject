"""ZooProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import logout
from ZooApp import views

urlpatterns = [
    url(r'^zooapp/', include('ZooApp.urls')),
    url(r'^admin/', admin.site.urls,name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^animals/$',views.animals,name='animals'),
    url(r'^birds/$',views.birds,name='birds'),
    url(r'^donor/',views.donor,name='donor'),
    url(r'^search/animals/fetchall/',views.fetchall_animals,name='animals_fetchall'),
    url(r'^search/birds/fetchall/', views.fetchall_birds, name='birds_fetchall'),
    url(r'^login/$',views.userlogin,name='userlogin'),
    url(r'^contactus/$',views.contact,name='contactus'),
    url(r'^empview',views.empview,name='empview'),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/(?P<name>[a-z]+)/$',views.search,name='search'),
]
