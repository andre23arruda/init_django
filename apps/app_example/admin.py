from django.contrib import admin
from .models import Book, Genre

@admin.register(Book)
class BookRegister(admin.ModelAdmin):
    list_display = ('id', 'title', 'registered_at',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    autocomplete_fields = ['genre']


@admin.register(Genre)
class GenreRegister(admin.ModelAdmin):
    list_display = ('id', 'name', 'registered_at',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
