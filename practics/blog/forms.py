from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'preview_text', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News Title'
            }),
            "preview_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preview News'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'News content'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date News'
            },

            ),
        }
