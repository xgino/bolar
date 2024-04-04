from urllib import request
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, FormView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Sum, Q

#import own models

from .forms import LoginForm, RegisterForm
from .forms import UpdateUserForm

from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('Accounts:account')

    def form_valid(self, form):
        request = self.request
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now login')
            return redirect('Accounts:account')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('Accounts:login')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('Accounts:login')


@login_required
def account(request):
    user = request.user

    context = {
        
    }

    return render(request, 'account.html', context)
