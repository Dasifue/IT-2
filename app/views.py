from django.shortcuts import render

def render_index(request):
    context = {
        "name": "Erbol",
        "age": 17,
        "prof": "Programmer",
        "skills": ["Python", "C++", "JS", "MySQL"]
    }
    return render(request, "index.html", context)
