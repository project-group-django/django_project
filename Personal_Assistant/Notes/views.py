# Create your views here.
from .utils import get_mongodb 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views import View
from .forms import NoteForm
from .models import Tag, Note
from .forms import YourTagFilterForm  # Replace with the actual name of your form class

import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi


#@login_required
def notes_view(request):
    # Retrieve the notes for the user
    notes = Note.objects.filter(note=id)
    return render(request, 'notes/note.html', {'notes': notes})  


#@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            #note = form.save(commit=False)
            note = Note(note='ggg   ggdg  e dfd d d d')
            note.save()           
            tags = form.cleaned_data['tags'].split(',')
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())  # Get or create the tag
                note.tags.add(tag)  # Add the tag to the note
            #return redirect(to='notes:note')
            return render(request, 'notes/note.html', {'form': form})
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})


#@login_required
def note_list(request):
    form = YourTagFilterForm(request.GET)
    notes = Note.objects.all()  # Отримуємо всі нотатки

    if form.is_valid():
        tags = form.cleaned_data['tags']
        if tags:
            # Фільтруємо нотатки за тегами
            notes = notes.filter(tags__in=tags)

    context = {
        'form': form,
        'notes': notes,
    }
    return render(request, 'notes/note_list.html', context)

#@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'notes/delete_note.html', {'note': note})

#@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})