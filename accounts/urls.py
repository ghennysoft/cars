from django.urls import path
from .views import Logout, Register, Login, profile, UpdateUser

app_name='accounts'

urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('update_profile/<int:pk>', UpdateUser, name='update_profile'),
]
