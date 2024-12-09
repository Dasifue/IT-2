from django.shortcuts import render 
 
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