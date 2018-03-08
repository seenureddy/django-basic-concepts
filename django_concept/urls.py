from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django_concept import views
from braintreeapp import views as braintreeappviews

handler404 = 'basic_dj.views.error404'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^library/', include('basic_dj.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^braintree/clienttoken/', braintreeappviews.clienttoken, name='client_token'),
    url(r'^braintree/checkout/', braintreeappviews.checkout, name='payments_checkout'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
