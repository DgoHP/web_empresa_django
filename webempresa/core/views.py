from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')


def store(request):
    return render(request, 'core/store.html')


