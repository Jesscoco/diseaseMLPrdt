from django.urls import path, include
from prediction import views

urlpatterns = [
    path('', views.index),
    path('contact/',views.contact, name='contact'),
  #  path ('about-us/', views.about),
  
]