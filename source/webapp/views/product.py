from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from accounts.forms import ReviewForm
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

class ProductAddView(PermissionRequiredMixin, CreateView):
    model = Product
    fields=['name', 'category','description','image']
    template_name = 'product/add.html'
    permission_required = 'webapp.add_product'
    permission_denied_message = 'Только модераторы могут добавлять товары и услуги!'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.pk})


class ProductEditView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'category','description','image']
    template_name = 'product/edit.html'
    permission_required = 'webapp.change_product'
    permission_denied_message = 'Только модераторы могут добавлять товары и услуги!'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.pk})

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_object_name = 'product'
    success_url = 'webapp: main page'
    permission_required = 'webapp.delete_product'
    permission_denied_message = 'Только модераторы могут добавлять товары и услуги!'

    def get_success_url(self):
        return reverse('webapp:main page')