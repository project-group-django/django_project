
# Create your views here.

from django.shortcuts import render, redirect
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
    db = get_mongodb()
    notes = db.notes.find()
    
    return render(request, 'notes/index.html', context={'notes': notes})

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



        # for quote_ in quotes:
            #     quot = Quote(quote=quote_.get("quote"),
            #                     tags=quote_.get("tags"),
            #                     author=quote_.get('author'),
            #                     )
                
            #     quot.save()   

            # if request.method == 'POST':
            #     form = QuoteForm(request.POST)
            #     if form.is_valid():
            #         # quote = form.save(commit=False)
            #         # quote.user = request.user
            #         # quote.save()
            #         # choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
            #         # for tag in choice_tags.iterator():
            #         #     quote.tags.add(tag)
            #         # author = form.save(commit=False)
            #         # author.user = request.user
            #         # author.save()
            #            # choice_author = Author.objects.filter(name__in=request.POST.getlist('author'), user=request.user)             
            
            #         for quote in quotes:
            
            # #author = db.authors.find_one({'fullname': quote['author']})    
            
            # #if author:
            #             db.quotes.insert_one({
            #                 'quote': quote['quote'],
            #                 'tags': quote['tags'],
            #                 'author': quote['author'],
            #             })
                    


        # from .utils import get_mongodb
        # from django.views import View
        # #from .forms import RegisterForm
        # from django.shortcuts import render, redirect
        # from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

        # from django.contrib import messages
        # #from django.core.paginator import Paginator

        # # Create your views here.
        # def main(request, page=1):
        #     db = get_mongodb()
        #     quotes = db.quotes.find()
        #     # per_page = 10
        #     # paginator = Paginator(list(quotes), per_page)
        #     # quotes_on_page = paginator.page(page)
        #     #return render(request, 'quotes/main.html')
        #     return render(request, 'quotes/index.html', context={'quotes': quotes})
        # #context={'quotes': quotes_on_page})
            
        # class RegisterView(View):   
        #     def quote(self, request):
                
        #         return render(request,'quotes/quote.html')
            
        #     def author(self, request):
                
        #         return render(request,'quotes/author.html')
            
        #     def tag(self, request):
                
        #         return render(request,'quotes/tag.html')

        # def quote(request):
        #     client = MongoClient('mongodb://localhost:27017') 
        #     db = client['hw']
        #     quotes_collection = db['quotes']
            
        #     form = QuoteForm(request.POST)
        #     if form.is_valid():
        #         # rest of your code
        #     else:
        #         print(form.errors)
