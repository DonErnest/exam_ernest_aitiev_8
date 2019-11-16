from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import UserSignUpForm, UserChangeForm, UserPasswordChangeForm


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'main_page'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = 'webapp:main page'


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:main page')
    else:
        form = UserSignUpForm()
    return render(request, 'register.html', context={'form': form})


class UserDetailedView(DetailView):
    model = User
    template_name = 'user/detailed.html'
    context_object_name = 'user_obj'


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'user/update.html'

    def get_success_url(self):
        return reverse('accounts:user detailed', kwargs={'pk':  self.object.pk})

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user/password_change.html'
    form_class = UserPasswordChangeForm
    context_object_name = 'user_obj'


    def get_success_url(self):
        return reverse('accounts:login')

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']