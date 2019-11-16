from django.db.models import Avg, Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

from accounts.forms import ReviewForm
from accounts.models import Review
from webapp.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

class ProductDetailedView(DetailView):
    model = Product
    template_name = 'product/product_detailed.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context=super(ProductDetailedView, self).get_context_data()
        context['form'] = ReviewForm()
        return context

class ProductAddView(CreateView):
    model = Product
    fields=['name', 'category','description','image']
    template_name = 'product/add.html'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.pk})


class ProductEditView(UpdateView):
    model = Product
    fields = ['name', 'category','description','image']
    template_name = 'product/edit.html'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_object_name = 'product'
    success_url = 'webapp: main page'

    def get_success_url(self):
        return reverse('webapp:main page')