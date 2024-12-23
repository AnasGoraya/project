
from django.contrib import admin
from django.urls import path,include
from CV import views

urlpatterns = [
      path('index',views.index,name="index"),
      path('signup',views.signup,name="signup"),
      path('',views.login,name="login"),
]
