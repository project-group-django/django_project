from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('news/', views.display_requests_page, name='news'),  

]