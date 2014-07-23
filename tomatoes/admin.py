from django.contrib import admin

# Register your models here.

from tomatoes.models import Movie, Favorite

admin.site.register(Movie)
admin.site.register(Favorite)