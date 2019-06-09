from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from django.contrib.auth.models import User
from .models import Profile, Portfolio


def welcome_page(request):
    return render(request, 'welcome.html')


def chatbot_page(request):
    context = {
        'followed_portfolios': Portfolio.objects.filter(followed=True),
        'not_followed_portfolios': Portfolio.objects.filter(followed=False)
    }

    print("view called")

    for portfolio in Portfolio.objects.filter(followed=True):
        print(portfolio.profile.name)

    return render(request, 'chatbot.html', context)


def imagetagging_page(request):
    return render(request, 'imagetagging.html')
