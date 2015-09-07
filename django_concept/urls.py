from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

handler404 = 'basic_dj.views.error404'
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^library/', include('basic_dj.urls')),
                       url(r'^$', 'django_concept.views.home', name='home'),
                       url(r'^braintree/clienttoken/', 'braintreeapp.views.clienttoken', name='client_token'),
                       url(r'^braintree/checkout/', 'braintreeapp.views.checkout', name='payments_checkout'),
                       )

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
