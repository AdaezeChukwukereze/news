from django.shortcuts import render


def base(request):
    return render(request, 'App/base-template.html')


def home(request):
    return render(request,'App/home-template.html')


def about(request):
    return render(request, 'App/about-template.html')




