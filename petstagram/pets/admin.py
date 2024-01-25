from django.contrib import admin

from petstagram.pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    class Meta:
        list_display = "__all__"
