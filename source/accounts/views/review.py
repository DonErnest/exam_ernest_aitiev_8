from _ast import Delete

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.forms import ReviewForm
from accounts.models import Review
from webapp.models import Product


class AddReviewView(LoginRequiredMixin, CreateView):
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


class EditReviewView(UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/edit.html'

    def test_func(self):
        self.object = self.get_review()
        return self.request.user.has_perm('accounts.change_review') or self.request.user.pk == self.object.author.pk

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.product.pk})

    def get_review(self):
        review_pk = self.kwargs.get('pk')
        review = get_object_or_404(Review,pk=review_pk)
        return review


class DeleteReviewView(UserPassesTestMixin, DeleteView):
    model = Review
    context_object_name = 'review'
    template_name = 'review/delete_confirm.html'

    def get_review(self):
        review_pk = self.kwargs.get('pk')
        review = get_object_or_404(Review,pk=review_pk)
        return review

    def test_func(self):
        self.object = self.get_review()
        return self.request.user.has_perm('accounts.change_review') or self.request.user.pk == self.object.author.pk

    def get_success_url(self):
        return reverse('webapp:product detailed', kwargs={'pk': self.object.product.pk})