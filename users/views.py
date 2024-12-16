from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import UserRegistrationForm


def register(request):

    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)

    context = {
        "form": form
    }
    return render(request, "register.html", context)


def login_view(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = "Не удалось авторизоваться. Проверьте правильность данных"

    return render(request, "login.html", {"message":message})


def logout_view(request):
    logout(request)
    return redirect('login')

