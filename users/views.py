from django.shortcuts import render, redirect
from django.contrib.auth import login as _login, logout as _logout, authenticate
 
from .forms import UserCreationForm 
 
def register(request): 
    form = UserCreationForm() 
 
    if request.method == "POST": 
        form = UserCreationForm(data=request.POST) 
        if form.is_valid(): 
            form.save(commit=True) 
 
    context = { 
        'form': form 
    } 
    return render(request, 'register.html', context)


def login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            _login(request, user)
            return redirect('index')
        else:
            message = "Не повезло."
        
    context = {
        "message": message
    }
    return render(request, 'login.html', context)

def logout(request):
    _logout(request)
    return redirect('login')
