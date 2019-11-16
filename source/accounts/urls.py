from django.urls import path

from accounts.views import UserLogoutView, register_view, UserLoginView
from accounts.views.review import AddReviewView, EditReviewView, DeleteReviewView

urlpatterns=[
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),

    path('products/<int:pk>/revies/add/', AddReviewView.as_view(), name='add review'),
    path('reviews/<int:pk>/edit/', EditReviewView.as_view(), name='edit review'),
    path('reviews/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete review')
]


app_name='accounts'