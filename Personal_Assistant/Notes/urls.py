from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
#from .views import RegisterView

#from .forms import LoginForm

app_name = "notes"

urlpatterns = [
    # ... інші URL-адреси ...
    path('', views.main, name='main'),  # URL-адреса для головної сторінки
    path('note/', views.note, name='note'),         
    path('tags/', views.tags, name='tags'),
]
