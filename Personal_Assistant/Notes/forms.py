from django import forms
from . models import Note, Tag


class YourTagFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class NoteForm(forms.ModelForm):
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Note
        fields = ['note']
        widgets = {
            'note': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        note = super().save(commit=False)
        #note.user = self.user
        if commit:
            note.save()
            self.save_m2m()
        # Обробка тегів
        tags_str = self.cleaned_data['tags']
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            note.tags.add(tag)
        return note

