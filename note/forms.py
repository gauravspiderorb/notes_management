from django import forms
from .models import ModelNote


# creating a form
class FormNote(forms.ModelForm):
    title = forms.CharField(
        max_length=100, required=True,
        label='title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title',
                'class': 'form-control'
            })
    )

    description = forms.CharField(
        required=True,
        label='description',
        widget=forms.Textarea(
            attrs={
                # 'class': 'demo-textarea',
                'rows': '4',
                'cols': '50',
                'placeholder': 'description',
                'class': 'form-control'
            })
    )

    # create meta class
    class Meta:
        model = ModelNote
        fields = {'title', 'description'}
