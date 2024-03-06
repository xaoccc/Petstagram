from django.shortcuts import get_object_or_404
from petstagram.pets.models import Pet


class GetPetBySlugAndOwnerMixin:
    def get_object(self, queryset=None):
        user_pk = self.kwargs.get('pk')
        pet_slug = self.kwargs.get('pet_slug')
        return get_object_or_404(Pet, owner=user_pk, slug=pet_slug)