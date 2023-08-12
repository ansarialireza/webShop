from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('register/',user_register, name='register'),
    path('profile/',profile, name='profile'),


    path('AddToWish/<int:id>/',AddToWish, name='AddToWish'),
    path('RomeveToWish/<int:id>/',RomeveToWish, name='RomeveToWish'),
    path('LikeComment/<int:id>/',LikeComment, name='LikeComment'),
    path('DisLikeComment/<int:id>/',DisLikeComment, name='DisLikeComment'),
]
