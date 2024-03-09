from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.common.forms import CommentForm
from petstagram.mixins.views_mixins import GetPetBySlugAndOwnerMixin, ProfileOwnerMixin, PetOwnerMixin
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm

UserModel = get_user_model()


class AddPetView(CreateView, LoginRequiredMixin):
    template_name = 'pets/pet-add-page.html'
    form_class = PetCreateForm

    def get_success_url(self):
        return reverse_lazy('profile-show', kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DetailsPetView(GetPetBySlugAndOwnerMixin, LoginRequiredMixin, DetailView):
    model = Pet
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['all_photos'] = self.object.photo_pet.all()
        return context


class EditPetView(PetOwnerMixin, GetPetBySlugAndOwnerMixin, LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    form_class = PetEditForm
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('pet-show', kwargs={"pk": self.request.user.pk, "pet_slug": self.object.slug})

class DeletePetView(PetOwnerMixin, GetPetBySlugAndOwnerMixin, LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy('profile-show', kwargs={"pk": self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context




