from django.db import models
from .slugify import unique_slugify


class BookManager(models.Model):
    """ Book title counts """
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Publisher(models.Model):
    """ Create Publisher with their credentials """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    slug = models.SlugField(unique=True)
    publisher_file = models.FileField(upload_to='publisher_upload_file_name')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super(Publisher, self).save(*args, **kwargs)

    def publisher_upload_file_name(self, publisher_doc):
        return '/'.join('content', self.name, publisher_doc)


class Author(models.Model):
    """ Author credentials """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=4)
    email = models.EmailField(blank=True)
    author_slug = models.SlugField(unique=True)

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)


class Book(models.Model):
    """ Book credentials """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    objects = BookManager()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.title)
        return super(Book, self).save(*args, **kwargs)
