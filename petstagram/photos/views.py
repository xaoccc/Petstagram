from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.common.forms import CommentForm
from petstagram.mixins.views_mixins import ProfileOwnerMixin
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['likes'] = self.object.photolike_set.all()
        context['comments'] = self.object.photocomment_set.all()
        return context

class PhotoEditView(LoginRequiredMixin, ProfileOwnerMixin, UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return '/'


class PhotoDeleteView(LoginRequiredMixin, ProfileOwnerMixin, DeleteView):
    model = Photo
    template_name = 'photos/photo-delete-page.html'

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhotoEditForm(initial=self.object.__dict__)
        return context

