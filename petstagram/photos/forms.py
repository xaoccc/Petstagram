from django import forms
from petstagram.photos.models import Photo, Pet


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        tagged_pets = forms.ModelMultipleChoiceField(queryset=Pet.objects.all(), widget=forms.CheckboxSelectMultiple,
                                                     label="Tag Pets")
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']

class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ['photo']
