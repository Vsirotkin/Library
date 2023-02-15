import uuid
from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a Genre')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text='Enter language of the book')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=50, help_text='Brief Description')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 characters long')
    genre = models.ManyToManyField(Genre, help_text='select a Genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='unique ID')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, related_name='book')
    imprint = models.CharField(max_length=50)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)

    LOAN_STATUS = [
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    ]
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Status')

    class Meta:
        ordering = ['due_back']
        permissions = (('can mark_returned', 'set book as returned'),)

    def __str__(self):
        # return '{0} ({1})'.format(self.id, self.book.title)
        return f'{self.imprint} - {self.book.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
