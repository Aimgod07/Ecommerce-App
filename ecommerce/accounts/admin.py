from django.contrib import admin
from .models import Profile
# Register your models here.
admin .site.register(Profile)

#why is it important to register models in admin.py file?
#Registering models in the admin.py file is important because it allows you to manage and manipulate your application's data through Django's built-in admin interface. By registering a model, you make it accessible in the admin panel, enabling you to perform CRUD (Create, Read, Update, Delete) operations on the model's data without needing to create custom views or forms. This is especially useful for site administrators and developers for quick data management and testing during development.