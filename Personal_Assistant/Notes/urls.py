from . import views
from django.urls import path

app_name = 'notes'

urlpatterns = [
    # ... other URL patterns ...
   
    path('', views.notes_view, name='notes'),  # Assuming you have a view named notes_view
    path('add_note/', views.add_note, name='add_note'),
    path('note_list/', views.note_list, name='note_list'),    
    path('notes/note/', views.notes_view, name='note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    
    # ... other URL patterns ...
]


