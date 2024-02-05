from django import forms
from petstagram.common.models import PhotoComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': "Add comment here..."})
        }

class SearchForm(forms.Form):
    pet_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Find pet...',
                'is_required': True
            }
        )
    )

