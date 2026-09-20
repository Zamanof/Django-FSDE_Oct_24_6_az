from django import forms
from unicodedata import category

from notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'tags']

        labels = {
            'title': 'Ad',
            'content': 'Mətn',
            'category': 'Kateqoriya',
            'tags': 'Teqlər'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Qeydin adini daxil edin",
            }),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': "Qeydinizi yazin",
                    'rows': 5,
                }),
            'category': forms.Select(attrs={
                'class': 'form-select mb-3',
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-select mb-3',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if title.lower().strip().startswith('test'):
            raise forms.ValidationError("Ad test sözü ilə başlaya bilməz")
        return title
