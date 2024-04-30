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


def main(request, page=1):
    # db = get_mongodb()
    notes = db.notes.find()
    pass

    return render(request, 'notes/note.html', context={'notes': notes})


def notes_view(request):
    # Retrieve the notes for the user
    notes = Note.objects.filter(note=id)
    return render(request, 'notes/note.html', {'notes': notes})  

# @login_required
# def tags(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             tag = form.save(commit=False)

#             tag.save()
#             return redirect(to='notes:main')
#         else:
#             return render(request, 'notes/tag.html', {'form': form})

#     return render(request, 'notes/tag.html', {'form': TagForm()})

@login_required
def note(request):
    client = MongoClient('mongodb://localhost:27017') 
    db = client['hw']
    notes_collection = db['notes']

    form = NoteForm(request.POST)
    if form.is_valid():
        note_data = form.cleaned_data  # Get the cleaned data from the form
                # Insert the document into the 'notes' collection
        notes_collection.insert_one({
            'note': note_data['note'],
            'tags': note_data['tags'],          
        })
        # No need to call save on the collection, as insert_one already saves the document
        return redirect(to='notes:main')
    else:
        print(form.errors)
    # If the form is not valid, you might want to handle the error or display the form again
    # For now, we'll just return to the main view
    return render(request, 'notes/note.html', {'form': NoteForm()})
    # else:
    #     #     return render(request, 'quotes/quote.html', {"tags": tags, 'form': form})

    # #return render(request, 'quotes/quote.html', {"tags": tags, 'form': QuoteForm()})
    #     return render(request, 'quotes/quote.html', {'form': QuoteForm()})

#@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    form = YourTagFilterForm(request.GET)

    if form.is_valid():
        tags = form.cleaned_data['tags']
        if tags:
            # Фільтруємо нотатки за тегами
            notes = Note.objects.filter(tags__in=tags)
            # Вибираємо одну з відповідних нотаток
            note = notes.filter(id=note_id).first()

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'notes/note_detail.html', context)

@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to='notes:main')

@login_required
def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect(to='notes:main')

#@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            #note = form.save(commit=False)
            note = Note(note='ggg   ggdg  e dfd d d d')
            note.save()
            #note.save()  # Save the note instance first
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
def filter_notes_by_tags(request):
    if request.method == 'GET':
        form = YourTagFilterForm(request.GET)
        if form.is_valid():
            # Process the form data here
            pass
    else:
        form = YourTagFilterForm()
    return render(request, 'notes/filter_notes_by_tags.html', {'form': form})


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