from django import forms
from .models import Book

class BookForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForms, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Book
        labels = {
            'title': 'Title',
            'genre': 'Genre',
            'author': 'Author',
        }
        fields = list(labels.keys())

    def clean(self):
        return self.cleaned_data