from django.contrib import admin
from django.urls import path
from . import views
from chat.models import Room,Message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
]