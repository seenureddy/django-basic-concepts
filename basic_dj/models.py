from django.db import models


class BookManager(models.Model):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    objects = BookManager()

    def __unicode__(self):
        return self.title
