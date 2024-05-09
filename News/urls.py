from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('news/', views.display_requests_page, name='news'),
    path('money/', views.money, name='money'),
    path('weather/', views.weather, name='weather'),

]