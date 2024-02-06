from petstagram.pets.models import Pet
from django import forms
from petstagram.mixins.forms_mixins import ReadOnlyFieldsMixin, DisabledFieldsMixin


class PetBaseForm(forms.ModelForm):
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

class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm, DisabledFieldsMixin):
    disabled_fields = ('birthdate',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_disabled()

    def clean_birthdate(self):
        return self.instance.birthdate

class PetDeleteForm(PetBaseForm, ReadOnlyFieldsMixin):
    readonly_fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_readonly()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance



