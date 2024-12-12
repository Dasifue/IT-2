from django.shortcuts import render

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
