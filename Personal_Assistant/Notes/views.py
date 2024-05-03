from .utils import get_mongodb 
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import NoteForm
from .models import Tag, Note
from .forms import YourTagFilterForm,YourTagForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def notes_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'Notesapp/note.html', {'notes': notes})  

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note_text = form.cleaned_data['note']
            user = request.user
            note = Note.objects.create(user=user, note=note_text)
            tags = form.cleaned_data['tags'].split(',')
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(user=user, name=tag_name.strip())
                note.tags.add(tag)
            return redirect('notes:note_list')
    else:
        form = NoteForm()
    return render(request, 'Notesapp/add_note.html', {'form': form})



@login_required
def note_list(request):
    form = YourTagFilterForm(request.GET)
    
    notes = Note.objects.filter(user=request.user)

    if form.is_valid():
        tags = form.cleaned_data['tags']
        if tags:
            notes = notes.filter(tags__in=tags)

    user_tags = Tag.objects.filter(note__user=request.user).distinct()

    
    context = {
        'form': form,
        'notes': notes,
        'user_tags': user_tags,
    }
    
    return render(request, 'Notesapp/note_list.html', context)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.user != request.user:
        return HttpResponse("Ви не маєте права видаляти цю нотатку.")
    
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'Notesapp/delete_note.html', {'note': note})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.user != request.user:
        return HttpResponse("Ви не маєте права редагувати цю нотатку.")
    
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
@login_required
def edit_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
        if tag.user != request.user:
            return HttpResponse("Ви не маєте права редагувати цей тег.")
        if request.method == 'POST':
            form = YourTagForm(request.POST, instance=tag)
            if form.is_valid():
                form.save()
                return redirect('notes:tag_edit_success', tag_id=tag_id) 
        else:
            form = YourTagForm(instance=tag)
        return render(request, 'Notesapp/edit_tag.html', {'form': form})
    except Tag.DoesNotExist:
        return HttpResponse("Тег не існує.")


    
@login_required   
def delete_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
        if tag.user != request.user:
            return HttpResponse("Ви не маєте права видаляти цей тег.")
        if request.method == 'POST':
            tag.delete()
            return redirect('notes:tag_delete_success', tag_id=tag_id)  
        return render(request, 'Notesapp/delete_tag.html', {'tag': tag})
    except Tag.DoesNotExist:
        return HttpResponse("Тег не існує.")

@login_required
def tag_list(request):
    tags = Tag.objects.filter(user=request.user)

    context = {
        'tags': tags,
    }
    return render(request, 'Notesapp/tag_list.html', context)