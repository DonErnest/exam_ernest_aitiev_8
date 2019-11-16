from django.urls import path

from webapp.views import IndexView
from webapp.views.product import ProductDetailedView, ProductEditView, ProductDeleteView, ProductAddView

urlpatterns=[
    path('', IndexView.as_view(), name='main page'),
    path('products/<int:pk>/', ProductDetailedView.as_view(), name='product detailed'),
    path('products/add/', ProductAddView.as_view(), name='add product'),
    path('products/<int:pk>/edit', ProductEditView.as_view(), name='edit product'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='delete product'),
]


app_name='webapp'