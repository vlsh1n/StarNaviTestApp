from django.urls import path

from .views import Register, user_login, user_logout

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
]
