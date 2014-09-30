from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PublisherForm, BookForm, AuthorForm
from .models import Publisher, Book


def create_publisher(request):
    """ creates publisher form """
    # if request.method == 'GET':
    create_form = PublisherForm()
    if request.method == 'POST':
        create_form = PublisherForm(request.POST, request.FILES)
        if create_form.is_valid():
            publisher = create_form.save()
            return HttpResponseRedirect(reverse('detail_publisher',
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
    # author_id = int(request.GET['author'])
    # author_obj = Author.objects.get(pk=author_id)

    book_form = BookForm()
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save()
            return HttpResponseRedirect(reverse('detail_book',
                                                args=[book.slug, ]))
    context_instance = {"book_form": book_form}
    return render(request,
                  'basic_dj/create_book.html', context_instance)


def detail_book(request, book_slug):
    """ generating slug return """
    book = get_object_or_404(Book, slug=book_slug)
    authors = book.author.all()
    return render(request,
                  'basic_dj/detail_book.html',
                  {'book': book, 'authors': authors})


def create_author(request):
    """ creating author """
    author_form = AuthorForm()
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author = author_form.save()
            return HttpResponseRedirect(reverse(
                'create_book') + '?author=' + str(author.pk))
    context_instance = {"author_form": author_form}
    return render(request,
                  'basic_dj/create_author.html', context_instance)


def book_list(request):
    """ show list of books for authors """
    books = Book.objects.all().order_by('-publication_date')
    paginator = Paginator(books, 2)      # show book list per page 2
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page('1')
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        books = paginator.page(paginator.num_pages)
    return render_to_response('basic_dj/book_list.html',
                              {'books': books})
