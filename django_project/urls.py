from django.contrib import admin
from django.urls import path
from portfolio.views import Homepage,Partfolio,About
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Homepage.as_view(), name = 'home'),
    path('partfolio/',Partfolio.as_view(), name = 'partfolio'),
    path('about/',About.as_view(), name = 'about')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)