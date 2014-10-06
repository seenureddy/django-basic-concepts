from django.contrib import admin

from basic_dj.models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['email']}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
