from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm


class AddPetView(CreateView, LoginRequiredMixin):
    template_name = 'pets/pet-add-page.html'
    form_class = PetCreateForm
    success_url = reverse_lazy('profile-show', kwargs={"pk": User.objects.first().pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DetailsPetView(DetailView):
    model = Pet
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['all_photos'] = self.object.photo_pet.all()
        return context


class EditPetView(UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    success_url = reverse_lazy('profile-show', kwargs={"pk": User.objects.first().pk})
    form_class = PetEditForm
    slug_url_kwarg = 'pet_slug'


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('profile-show', kwargs={"pk": User.objects.first().pk})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context




