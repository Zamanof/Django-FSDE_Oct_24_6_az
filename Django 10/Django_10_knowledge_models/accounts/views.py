from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login, authenticate, logout


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['username_or_email'].strip()
            password = form.cleaned_data['password']

            user = authenticate(request, username=identifier, password=password)
            if user is None:
                User = get_user_model()
                try:
                    candidate = User.objects.get(email__iexact=identifier)
                except User.DoesNotExist:
                    candidate = None
            if user is not None:
                login(request, user)
                messages.success(request, "Siz uğurla daxil oldunuz")
            return redirect("accounts:dashboard")
        form.add_error("İstifadəçi adı və şifrə yanlışdır")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
            login(request, user)
            messages.success(request, "İstifadəçi uğurla yaradıldı")
            return redirect("accounts:dashboard")
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def register_success_view(request):
    return render(request, 'accounts/register_success.html')

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Saytı uğurla tərk etdiniz")
        return redirect("accounts:dashboard")
    return redirect("home")
