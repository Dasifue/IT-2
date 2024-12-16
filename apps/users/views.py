from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


from .forms import UserCreationForm

def register_view(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')

    return render(request, "register.html", {"form": form})


def login_view(request):
    message = ''

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
            message = 'Не удалось авторизоваться'

    return render(request, 'login.html', {'message': message})


def logout_view(request):
    logout(request)
    return redirect('login')