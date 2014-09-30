from django import forms
from .models import Publisher, Book, Author


class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        exclude = ('slug',)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = ('slug',)


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = ('author_slug', )
