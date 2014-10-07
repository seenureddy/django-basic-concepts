from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Publisher, Author, Book
from .forms import PublisherForm, BookForm, AuthorForm


@login_required
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


@login_required
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
    return render(request,
                  'basic_dj/detail_book.html',
                  {'book': book})


@login_required
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
    """ Show list of books """
    books = Book.objects.all().order_by('-publication_date')
    paginated_by = getattr(settings, 'BOOKS_PER_PAGE', 4)
    paginator = Paginator(books, paginated_by)      # show book list per page 2
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page('1')
    except EmptyPage:
        # If page is out of range (e.g. 99), deliver last page of results
        books = paginator.page(paginator.num_pages)
    return render_to_response('basic_dj/book_list.html',
                              dict(books=books))


def author_books_list(request, author_slug):
    """ Show all books written by an author """
    author = get_object_or_404(Author, slug=author_slug)
    author_books = author.books.all()
    return render_to_response('basic_dj/author_books_list.html',
                              dict(author=author, author_books=author_books))


def publisher_books_list(request, publisher_slug):
    """ Show all Books published by a publisher """
    publisher = get_object_or_404(Publisher, slug=publisher_slug)
    publisher_books = publisher.books.all()
    return render_to_response('basic_dj/publisher_books_list.html',
                              dict(publisher=publisher,
                                   publisher_books=publisher_books))


def index(request):
    """ Created index page to show all url for Publisher, Author, Book """
    return render(request, 'basic_dj/home.html')
