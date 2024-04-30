# from django.urls import path, include
from . import views
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.views import LoginView, LogoutView
# #from .views import RegisterView

from django.urls import path, include
from .views import note_detail 

app_name = 'Notes'

urlpatterns = [
    # ... other URL patterns ...
    #path('notes/', include('Notes.urls')),
    path('', views.notes_view, name='notes'),  # Assuming you have a view named notes_view
    path('add_note/', views.add_note, name='add_note'),
    path('note_list/', views.note_list, name='note_list'),
    path('note_detail/', views.note_detail, name='note_detail'),
    path('notes/note_detail/<int:note_id>/', note_detail, name='note_detail'),
    # ... other URL patterns ...
]

# app_name = "Notes"
# #from .forms import LoginForm

# #app_name = "Personal_Assistant"

# urlpatterns = [
#     # ... інші URL-адреси ...
#     path('', views.main, name="root"),  # URL-адреса для головної сторінки
#     path('notes/', include('Notes.urls')),        
#     #path('tags/', views.tags, name='tags'),
# ]
