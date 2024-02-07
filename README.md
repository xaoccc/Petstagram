# Petstagram
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

