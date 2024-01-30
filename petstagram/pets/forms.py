from petstagram.pets.models import Pet
from django import forms


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "birthdate", "pet_photo"]

        labels = {
            'name': ('Pet Name'),
            'birthdate': ('Date of Birth'),
            'pet_photo': ('Link to Image'),
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'birthdate': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'mm/dd/yyyy'}),
            'pet_photo': forms.TextInput(attrs={'placeholder': 'pet photo'})
        }

