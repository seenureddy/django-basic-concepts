from django.conf.urls import patterns, url

urlpatterns = patterns('basic_dj.views',
                       url(r'^create-publisher/$', 'create_publisher',
                           name='create_publisher'),
                       url(r'^detail-publisher/(?P<publisher_slug>[-\w]+)/$',
                           'detail_publisher', name='detail_publisher'),
                       url(r'^create-book/$',
                           'create_book', name='create_book'),
                       url(r'^detail-book/(?P<book_slug>[-\w]+)/$',
                           'detail_book', name='detail_book'),
                       url(r'^create-author/$',
                           'create_author', name='create_author'),
                       url(r'^books/$', 'book_list', name='book_list'),
                       url(r'^books/author/(?P<author_slug>[-\w]+)/$',
                           'author_books_list',
                           name='author_books_list'), )
