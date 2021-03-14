from django import forms
from .models import Book

class BookForms(forms.ModelForm):

    class Meta:
        model = Book
        labels = {
            'author': 'Autor',
            'title': 'Título'
        }
        fields = list(labels.keys())

    def clean(self):
        return self.cleaned_data