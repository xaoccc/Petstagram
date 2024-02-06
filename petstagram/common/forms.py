from django import forms
from petstagram.common.models import PhotoComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': "Add comment here..."})
        }
