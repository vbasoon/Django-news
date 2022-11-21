from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def index(request):
    context = {
        "title": "Main Page",
        'value': ['Honda', 'Toyota', 'Nissan']
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        "title": "About Page"
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        "title": "Contacts"
    }
    return render(request, 'main/contacts.html', context)
