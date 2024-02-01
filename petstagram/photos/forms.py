from django import forms
from petstagram.photos.models import Photo, Pet

class PhotoCreateForm(forms.ModelForm):
    tagged_pets = forms.ModelMultipleChoiceField(queryset=Pet.objects.all(), widget=forms.CheckboxSelectMultiple, label="Tag Pets")
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']