# Create your views here.
from .utils import get_mongodb 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views import View
from .forms import TagForm, NoteForm
from .models import Tag, Note

import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient('mongodb://localhost:27017') 
db = client.hw

def main(request, page=1):
    # db = get_mongodb()
    # notes = db.notes.find()
    pass

    return render(request, 'notes/note.html', context={'notes': notes})

def notes_view(request):
    db = get_mongodb()
    notes = db.notes_note.find()
    pass

    return render(request, 'notes/note.html', context={'notes': notes})    

@login_required
def tags(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)

            tag.save()
            return redirect(to='notes:main')
        else:
            return render(request, 'notes/tag.html', {'form': form})

    return render(request, 'notes/tag.html', {'form': TagForm()})

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

@login_required
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', {"note": note})

@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to='notes:main')

@login_required
def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect(to='notes:main')