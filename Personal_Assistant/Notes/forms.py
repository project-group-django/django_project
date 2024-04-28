from django.forms import CharField, TextInput, EmailField, PasswordInput
from django.contrib.auth.models import User, Note, Tag
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class TagForm(UserCreationForm):
    tags = CharField(max_length=19, required=True, widget=TextInput(attrs={"class": "form-control", }))
    
class NoteForm(forms.Form):
    note = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    tags = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))  # Assuming tags are entered as a comma-separated string
    

    def clean_tags(self):
        tags_str = self.cleaned_data['tags']
        tags = [tags.strip() for tags in tags_str.split(',')]
        return tags



# class QuoteForm(AuthenticationForm):
#     quote = CharField(widget=TextInput(attrs={"class": "form-control"}))
#     tags = ListField(widget=ArraysInput(attrs={"class": "form-control"}))
#     author = CharField(widget=TextInput(attrs={"class": "form-control"}))

#     class Meta:
#         model = User
#         fields = ['quote', 'tags', 'author']
