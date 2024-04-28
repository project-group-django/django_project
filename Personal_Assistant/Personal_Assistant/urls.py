"""
URL configuration for Personal_Assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Personal_Assistant/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', views.notes_view, name='notes'),  # Assuming you have a view named notes_view
    # ... other URL patterns
]


# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls), 
#    # path("", include('Personal_Assistant.urls')),    
#     #path('notes/', include('Notes.urls')),
#     #path('users/', include('users.urls')),
#     ] 

