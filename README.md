# Petstagram

### Description
This is a social media app for pet lovers. Here you can:
- Register, Login, Update, Delete, View users
- Add, Update and Delete pets
- Add, Like and Comment pictures of your pets
- Move easily between pages
- Search pet by name

## Updated to v.1.01:
- Upgraded user management by added a custom User model and a Profile model linked to the user model
- The logged-in user now cannot add, edit and delete other profiles, pets or photos!
- TODO: 
- Repair the likes counter so each pet photo can have multiple likes
- Add more validators


Steps in creating a Django project:
1. Create the apps using the command $ python manage.py startapp app_name. For each app do this:
2. Setup  
   * Add the app in INSTALLED_APPS, like so: 'project_name.app_name' if the app folder is inside the project folder.
   * Setup DATABASES. For PostgreSQL:  
   ```
    'default': {
     'ENGINE': 'django.db.backends.postgresql',
     'NAME': 'car_collection_db',
     'USER': 'postgres',
     'PASSWORD': 'postgres',
     'HOST': '127.0.0.1',
     'PORT': '5432',
   }
   ```
   * Setup Staticfiles dirs: 
   ```
   STATIC_URL = 'static/'
   STATICFILES_DIRS = (BASE_DIR / 'static',)
   ```
   * Verify apps names in apps.py, like so: 
   `name = 'project_name.app_name'`   
   The name here should be sa same as the one in settings.py
   * Setup url path for each app in urls.py of the project:
   ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('project_name.main_app.urls')),
        path('path1/', include('project_name.app1_name.urls')),
        path('path2/', include('project_name.app2_name.urls')),
   ]
   ```
   
3. Create models 
   * Add built-in validators
   * Add custom validators in validators.py like so:
   ```
   from django.core.exceptions import ValidationError   
   def custom_validator(value):   
      if (logic, value):
         raise ValidationError('error_message')
   ```
   * Create the database (if not created)
   * ADD CUSTOM USER MODEL BEFORE ANY MIGRATIONS
   * Make migrations
   * Migrate

4. Create urls for each view/template inside each app:
   `path('path1/', views.view_name, name='template-name'),` for FBV  
   `path('path1/', views.ViewName.as_view(optional parameters), name='template-name'),` for CBV
5. Create views
6. Create forms in new file forms.py
7. Create templates
8. Add styles
9. Add media

### Notes
* Use Class Based Views
* If form is needed, always create forms.py, so you can customize it later if required
* When model is called in the form, this model is not necessary to be called again in the view
* Use form.as_div in the template whenever possible. Using forms.py it is much easier
* Follow SOLID!


### CBVs attributes:
* DetailView:  
**model: required**   
template_name:   
context_object_name:   
slug_field and slug_url_kwarg:   
* CreateView:  
**model: required**  
template_name:  
**form_class/fields: required**  
success_url:
* UpdateView:  
**model: required**  
template_name:  
**form_class/fields: required**  
success_url:   
* ListView:  
**model: required**  
template_name:  
context_object_name:  
paginate_by:  
ordering:  
* DeleteView:  
**model: required**  
template_ 
success_url:  
slug_field and slug_url_kwarg:  

### Useful CBV methods:  
* get_form()  
Customizing a form in UpdateView and other CBVs:  
```    
 def get_form(self, form_class=None):
     form = super().get_form(form_class)
     form.fields['FIELD_NAME'].ATTRIBUTE_NAME = 'VALUE'
     return form
```
* form_valid()  
Used often when we need to add field to the form instance in the view:  
```    
 def form_valid(self, form):
     form.instance.owner = self.request.user
     return super().form_valid(form)
```
* get_context_data()  
Working with model instance fields inside DeleteView/EditView:
 ```    
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_instance = self.get_object()
        context['form'].fields['FIELD_NAME'].widget.attrs['ATTRIBUTE_NAME'] = VALUE
```
* get_object()
If we need a specific instance of the model in the view, we can override get_object()
```
 def get_object(self, queryset=None):
     return Pet.objects.get(slug=self.kwargs['pet_slug'])
```
* get_queryset()
If we need to filter the current queryset (usually used when searching or filtering on some criteria):
```
 def get_queryset(self):
     queryset = MyViewModel.objects.filter(FILTER CRITERIA)
     return queryset
```
We can use even several querysets:  
```
def get_queryset(self):
  queryset1 = Model1.objects.all()
  queryset2 = Model2.objects.filter(some_field=some_value)
  return queryset1, queryset2

def get_context_data(self, **kwargs):
  context = super().get_context_data(**kwargs)
  queryset1, queryset2 = self.get_queryset()
  context['queryset1'] = queryset1
  context['queryset2'] = queryset2
  return context
```

* get_form_kwargs()
Often used in the DeleteView to get the instance of the object and pass it to the form,
If the delete view requires a form.   
Usually it goes with a get_form() method to apply readonly to all fields  
```
 def get_form_kwargs(self):
     kwargs = super().get_form_kwargs()
     kwargs['instance'] = self.object
     return kwargs
```

* Create Profile with User creation using signals:
In signals.py in the app (where is the views.py):
```
@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```
In apps.py inside the AccountsConfig:
```
    def ready(self):
        import project_name.app_name.signals
```
