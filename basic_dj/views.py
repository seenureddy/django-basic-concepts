from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from .forms import PublisherForm, BookForm
from .models import Publisher


def create_publisher(request):
    """ creates publisher form """
    # if request.method == 'GET':
    create_form = PublisherForm()
    if request.method == 'POST':
        create_form = PublisherForm(request.POST, request.FILES)
        if create_form.is_valid():
            publisher = create_form.save()
            return HttpResponseRedirect(reverse('basic_dj_detail',
                                                args=[publisher.slug, ]))
    context_instance = {"create_form": create_form}
    return render(request, 'basic_dj/create_publishers.html', context_instance)


def detail_publisher(request, publisher_slug):
    """ generates slug and retrun """
    publisher = get_object_or_404(Publisher, slug=publisher_slug)
    return render(request,
                  'basic_dj/detail_publishers.html', {'publisher': publisher})


def error404(request):
    return HttpResponseNotFound(render_to_string('404.html'))


def create_book(request):
    """ creates Book form """
    book_form = BookForm()
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save()
    context_instance = {"book_form": book_form} 
    return render(request,
                  'basic_dj/create_book.html', context_instance)
