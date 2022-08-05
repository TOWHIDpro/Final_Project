from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user, name="create_user"),
    path('test-page', views.index, name="index"),
    path('user-login', views.usr_login, name="user-login"),
    path('result', views.result, name="result"),
    path('all_result', views.all_result, name="all_result"),
   
]
