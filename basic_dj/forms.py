from django import forms
from basic_dj.models import Publisher


class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        exclude = ('slug',)
