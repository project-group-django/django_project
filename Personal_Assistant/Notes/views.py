from .utils import get_mongodb 
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import NoteForm
from .models import Tag, Note
from .forms import YourTagFilterForm,YourTagForm
from django.http import HttpResponse




def notes_view(request):
    notes = Note.objects.filter(note=id)
    return render(request, 'Notesapp/note.html', {'notes': notes})  


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Отримати дані з форми
            note_text = form.cleaned_data['note']
            # Створити нову нотатку з введеним текстом
            note = Note.objects.create(note=note_text)
            # Отримати теги з форми та додати їх до нотатки
            tags = form.cleaned_data['tags'].split(',')
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
                note.tags.add(tag)
            # Перенаправити на сторінку з нотатками або вивести успішне повідомлення
            return redirect('notes:note_list')
    else:
        form = NoteForm()
    return render(request, 'Notesapp/add_note.html', {'form': form})




def note_list(request):
    form = YourTagFilterForm(request.GET)
    notes = Note.objects.all() 

    if form.is_valid():
        tags = form.cleaned_data['tags']
        if tags:
            notes = notes.filter(tags__in=tags)

    context = {
        'form': form,
        'notes': notes,
    }
    return render(request, 'Notesapp/note_list.html', context)


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'Notesapp/delete_note.html', {'note': note})


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'Notesapp/edit_note.html', {'form': form})

def tag_delete_success(request, tag_id):
    return render(request, 'Notesapp/tag_delete_success.html', {'tag_id': tag_id})

def tag_edit_success(request, tag_id):
    return render(request, 'Notesapp/tag_edit_success.html')

def edit_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
        if request.method == 'POST':
            form = YourTagForm(request.POST, instance=tag)
            if form.is_valid():
                form.save()
                return redirect('notes:tag_edit_success', tag_id=tag_id) 
        else:
            form = YourTagForm(instance=tag)
        return render(request, 'Notesapp/edit_tag.html', {'form': form})
    except Tag.DoesNotExist:
        return HttpResponse("Tag does not exist.")


    
    
def delete_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
        if request.method == 'POST':
            tag.delete()
            return redirect('notes:tag_delete_success', tag_id=tag_id)  
        return render(request, 'Notesapp/delete_tag.html', {'tag': tag})
    except Tag.DoesNotExist:
        return HttpResponse("Tag does not exist.")


def tag_list(request):
    tags = Tag.objects.all()

    context = {
        'tags': tags,
    }
    return render(request, 'Notesapp/tag_list.html', context)

