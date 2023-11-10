from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrarse, name="registro"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"), 

]