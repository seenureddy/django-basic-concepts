from django.contrib import admin
from .models import Publisher, Author, Book


class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
