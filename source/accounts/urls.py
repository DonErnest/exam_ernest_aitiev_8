from django.urls import path

from accounts.views import UserLogoutView, register_view, UserLoginView

urlpatterns=[
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]


app_name='accounts'