from django.contrib import admin
from app2.views import *
from django.urls import path
app_name='s'
urlpatterns=[
    path('admin/', admin.site.urls),
    path('papaa/',papaa,name='papaa'),
]