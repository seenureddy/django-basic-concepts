from django.conf.urls import patterns, url

urlpatterns = patterns('basic_dj.views',
                       url(r'^create-publisher/$', 'create_publisher',
                           name='create_publisher'),
                       url(r'^detail-publisher/(?P<publisher_slug>[-\w]+)/$',
                           'detail_publisher', name='detail_publisher'),
                       url(r'^create-book/$',
                           'create_book', name='create_book'),
                       url(r'^detail-book/(?P<book_slug>[-\w]+)/$',
                           'detail_book', name='detail_book'), )
