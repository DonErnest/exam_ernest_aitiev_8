from _ast import Delete

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.forms import ReviewForm
from accounts.models import Review
from webapp.models import Product


class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/add.html'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.product.pk})

    def get_product(self):
        product_pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        return product

    def form_valid(self, form):
        self.product = self.get_product()
        self.object = self.product.reviews.create(**form.cleaned_data)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditReviewView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/edit.html'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.product.pk})

class DeleteReviewView(DeleteView):
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.product.pk})