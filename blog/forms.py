from django import forms
from .models import Article

class CreateArticleForm(forms.ModelForm):
    title = forms.CharField()
    class Meta:
        model= Article
        fields= [
            'title',
            'content',
            'author',
        ]