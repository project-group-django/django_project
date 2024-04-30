from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('new/', views.contact_create, name='contact_create'),
    path('<int:pk>/update/', views.contact_update, name='contact_update'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('search/', views.contact_search, name='contact_search'),
    path('birthdays/', views.upcoming_birthdays, name='upcoming_birthdays'),
]