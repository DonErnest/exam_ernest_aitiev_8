from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render

from accounts.forms import UserSignUpForm

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'main_page'
    redirect_authenticated_user = True

# def login_view(request, *args, **kwargs):
#     context={}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         redirect_path = request.GET.get('next')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if redirect_path:
#                 return redirect(redirect_path)
#             return redirect('webapp:main_page')
#         else:
#             context['has_error']=True
#             context['next']=redirect_path
#             context['username']=username
#
#     else:
#         context={'next': request.GET.get('next')}
#     return render(request, 'login.html', context=context)


class UserLogoutView(LogoutView):
    next_page = 'webapp:main page'


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('webapp:main page')
    else:
        form=UserSignUpForm()
    return render(request, 'register.html', context={'form': form})