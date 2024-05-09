from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UserFile
from django.http import HttpResponseBadRequest
import os



def file_list(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            return redirect('file_list') 
    else:
        form = FileUploadForm()

    category = request.GET.get('category', '')  
    files = UserFile.objects.filter(user=request.user)

    if category:
        files = files.filter(category=category)

    return render(request, 'filemanager/file_list.html', {'files': files, 'form': form})

def delete_file(request, file_id):
    try:
        file_to_delete = UserFile.objects.get(id=file_id, user=request.user)
    except UserFile.DoesNotExist:
        return HttpResponseBadRequest("Недопустимий запит")

    if os.path.exists(file_to_delete.file.path):
        os.remove(file_to_delete.file.path)
        file_to_delete.delete()
        return redirect('file_list')
    else:
        return HttpResponseBadRequest("Файл не існує")
