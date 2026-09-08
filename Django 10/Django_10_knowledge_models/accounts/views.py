from django.shortcuts import render

from accounts.forms import RegisterForm, LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, "accounts/dashboard.html", {"form": form})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return render(request, 'accounts/register_success.html')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def register_success_view(request):
    return render(request, 'accounts/register_success.html')


def logout_view(request):
    pass
