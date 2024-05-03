from . import views
from django.urls import path

app_name = 'notes'

urlpatterns = [
   
    path('', views.notes_view, name='notes'), 
    path('add_note/', views.add_note, name='add_note'),
    path('note_list/', views.note_list, name='note_list'),    
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('edit_tag/<int:tag_id>/', views.edit_tag, name='edit_tag'),
    path('delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('tag_edit_success/<int:tag_id>/', views.tag_edit_success, name='tag_edit_success'),
    path('tag_delete_success/<int:tag_id>/', views.tag_delete_success, name='tag_delete_success'),
    path('tag_list/', views.tag_list, name='tag_list'),
    

]


