from django.urls import path, include

from . import views

app_name = "News"

urlpatterns = [
    path("", views.main, name="root"),
    path('users/', include('Users.urls')),
]