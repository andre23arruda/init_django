from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookRegister(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'registered_at',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)