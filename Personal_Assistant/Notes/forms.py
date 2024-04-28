from django import forms
from notes.models import Note, Tag  # Assuming your Note and Tag models are in the same app

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']  # Assuming 'name' is the field for tag names in your Tag model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']  # Assuming 'note' is the field for note content in your Note model
        widgets = {
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'] = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_tags(self):
        tags_str = self.cleaned_data['tags']
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
        return tags
    






# from django.forms import CharField, TextInput, EmailField, PasswordInput
# from django.contrib.auth.models import User, Note, Tag
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django import forms

# class TagForm(UserCreationForm):
#     tags = CharField(max_length=19, required=True, widget=TextInput(attrs={"class": "form-control", }))
    
# class NoteForm(forms.Form):
#     note = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     tags = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))  # Assuming tags are entered as a comma-separated string
    

#     def clean_tags(self):
#         tags_str = self.cleaned_data['tags']
#         tags = [tags.strip() for tags in tags_str.split(',')]
#         return tags



# class QuoteForm(AuthenticationForm):
#     quote = CharField(widget=TextInput(attrs={"class": "form-control"}))
#     tags = ListField(widget=ArraysInput(attrs={"class": "form-control"}))
#     author = CharField(widget=TextInput(attrs={"class": "form-control"}))

#     class Meta:
#         model = User
#         fields = ['quote', 'tags', 'author']
