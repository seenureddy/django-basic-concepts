from django import forms
from .models import Publisher, Book


class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        exclude = ('slug',)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
