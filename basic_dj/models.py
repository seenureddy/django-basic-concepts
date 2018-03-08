from django.db import models
from django.utils.translation import ugettext_lazy as _

from .slugify import unique_slugify
from .storage import upload_document


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(_('created'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class BookManager(models.Manager):
    """ Book title counts """
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Publisher(TimeStampedModel):
    """ Create Publisher with their credentials """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    slug = models.SlugField(unique=True)
    publisher_file = models.FileField(upload_to=upload_document)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super(Publisher, self).save(*args, **kwargs)


class Author(models.Model):
    """ Author credentials """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=4)
    email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.email)
        return super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    """ Book credentials """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books')
    publication_date = models.DateField()
    objects = BookManager()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.title)
        return super(Book, self).save(*args, **kwargs)
