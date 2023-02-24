from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalogue.models import Book, BookInstance, Author


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # counting how many units each book has
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    # counting the visits' number of the user
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instance_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'catalogue/index.html', context)


class BookListView(ListView):
    model = Book
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author
    paginate_by = 5


class AuthorDetailView(DetailView):
    model = Author
