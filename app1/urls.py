from django.contrib import admin
from app1.views import *
from django.urls import path
app_name='p'
urlpatterns=[
    path('admin/', admin.site.urls),
    path('mamma/',mamma,name='mamma'),
]