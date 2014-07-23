from django.contrib import admin

# Register your models here.

from tomatoes.models import Movie

admin.site.register(Movie)