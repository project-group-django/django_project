from django.shortcuts import render
from .news_parser import parse_news

def index(request):
    return render(request, 'Newsapp/index.html')

def display_requests_page(request):
    news = parse_news()
    return render(request, 'Newsapp/requests_page.html', {'news': news})

def money(request):
    return render(request, 'Newsapp/money.html')

def weather(request):
    return render(request, 'Newsapp/weather.html')