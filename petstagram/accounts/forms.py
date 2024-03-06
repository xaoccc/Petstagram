from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from petstagram.accounts.models import Profile


UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(user=user)
        if commit:
            profile.save()
        return user

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['profile_picture'].widget.attrs['placeholder'] = 'Profile Picture URL'

