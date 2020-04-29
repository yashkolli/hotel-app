from django.urls import path
from . import views

urlpatterns = [
    path('', views.newroom, name='newroom'),
    path('set_light/',views.set_light,name='set_light'),
    path('set_fan/',views.set_fan,name='set_fan'),
    path('billing/', views.billing, name='user-billing'),
]
