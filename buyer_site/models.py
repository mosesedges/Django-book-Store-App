from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# created a category model which the Book model inherit as a foreign key, so a Book object can't be created without first creating a category.


class Category(models.Model):
    name = models.CharField(max_length=110)

# below is an inner meta class that describe the singula and plurals of the outer class (Book) name

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name


# class Author(models.Model):
#     name = models.CharField(max_length=256)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name


# below is a Book models with many fields including the DateTimeField which is why the timezone was imported from django utils.
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    year_of_publication = models.IntegerField()
    pages = models.IntegerField(null=False, )
    price = models.FloatField(default=0.00)
    long_description = models.TextField()
    thumbnail = models.CharField(max_length=250, null=True)
    posted_on = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=256, default='mary')

# the ordering in the meta class sets the ordering for most current first
    class Meta:
        verbose_name = ('Book')
        verbose_name_plural = ('Books')
        ordering = ('-posted_on',)

    def __str__(self):
        return self.title

# below is the Review model responsible for the reviews on the Book_detail views.


class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-created_at',)
