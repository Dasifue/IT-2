from django.shortcuts import render


from .forms import UserCreationForm

def register_view(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request, "register.html", {"form": form})
