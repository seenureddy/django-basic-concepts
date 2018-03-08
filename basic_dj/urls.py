from django.conf.urls import url
from basic_dj.views import (
    index, create_publisher, book_list, detail_publisher,\
    detail_book, publisher_books_list, author_books_list, create_book,\
    create_author
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create-publisher/$', create_publisher,
        name='create_publisher'),
    url(r'^detail-publisher/(?P<publisher_slug>[-\w]+)/$',
        detail_publisher, name='detail_publisher'),
    url(r'^create-book/$',
        create_book, name='create_book'),
    url(r'^detail-book/(?P<book_slug>[-\w]+)/$',
        detail_book, name='detail_book'),
    url(r'^create-author/$',
        create_author, name='create_author'),
    url(r'^books/$', book_list, name='book_list'),
    url(r'^books/author/(?P<author_slug>[-\w]+)/$',
        author_books_list, name='author_books_list'),
    url(r'^books/publisher/(?P<publisher_slug>[-\w]+)/$',
        publisher_books_list, name='publisher_books_list'),
]
