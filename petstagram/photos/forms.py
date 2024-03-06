from django import forms
from petstagram.photos.models import Photo, Pet


class PhotoBaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the kwargs
        super(PhotoBaseForm, self).__init__(*args, **kwargs)
        if user:
            # Filter the tagged_pets queryset by the owner
            self.fields['tagged_pets'].queryset = Pet.objects.filter(owner=user)
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']
        widgets = {
            'tagged_pets': forms.CheckboxSelectMultiple,
        }

class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ['photo']
