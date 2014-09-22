from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from basic_dj import forms as pforms
from basic_dj.models import Publisher
from django.shortcuts import get_object_or_404


def create_publisher(request):
    # if request.method == 'GET':
    create_form = pforms.PublisherForm()
    if request.method == 'POST':
        create_form = pforms.PublisherForm(request.POST, request.FILES)
        if create_form.is_valid():
            # file_doc = Publisher(publisher_file = request.FILES['publisher_file'])
            publisher = create_form.save()
            return HttpResponseRedirect(reverse('basic_dj_detail', args=[publisher.slug,]))
    context_instance = {"create_form": create_form}
    return render(request, 'basic_dj/create.html', context_instance)


def detail_publisher(request, publisher_slug):
    publisher = get_object_or_404(Publisher, slug=publisher_slug)
    return render(request, 'basic_dj/detail_publisher.html',{'publisher': publisher})
