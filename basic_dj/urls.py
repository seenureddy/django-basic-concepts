from django.conf.urls import include, patterns, url

urlpatterns = patterns('basic_dj.views',
    url(r'^create/$','create_publisher',name='basic_dj_create'),
    url(r'^(?P<publisher_slug>[-\w]+)/$','detail_publisher',name='basic_dj_detail'),
)
