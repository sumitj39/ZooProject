

from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^sumit/$',views.index,name='index'),
]