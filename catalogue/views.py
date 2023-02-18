from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalogue.models import Book, BookInstance, Author


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instance_available,
        'num_authors': num_authors,
    }
    return render(request, 'catalogue/index.html', context)


class BookListView(ListView):
    model = Book
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book
