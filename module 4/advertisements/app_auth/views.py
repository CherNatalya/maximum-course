from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'app_auth/login.html', {'user': username})
        return render(request, 'app_auth/register.html', {"error": "Ошибка. Проверьте все данные"})
    form = UserRegisterForm()
    return render(request, 'app_auth/register.html', {'form': form})


def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
