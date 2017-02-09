from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^', include('app.urls')),
               url(r'^', include('dauth.urls')),
               ]
