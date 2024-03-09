from django.shortcuts import get_object_or_404, redirect
from petstagram.pets.models import Pet


class GetPetBySlugAndOwnerMixin:
    def get_object(self, queryset=None):
        user_pk = self.kwargs.get('pk')
        pet_slug = self.kwargs.get('pet_slug')
        return get_object_or_404(Pet, owner=user_pk, slug=pet_slug)


class PetOwnerMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionError('You are not allowed to edit or delete this profile')
        return obj

class ProfileOwnerMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile.user != self.request.user:
            raise PermissionError('You are not allowed to edit or delete this content')
        return obj

class ProfileOwnerMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.profile.user != self.request.user:
            raise PermissionError('You are not allowed to edit or delete this content')
        return obj
