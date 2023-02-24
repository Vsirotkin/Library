from django.urls import path

from . import views

app_name = 'catalogue'
urlpatterns = [
    path('', views.index, name='index'),
    # books
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # authors
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    # path('', RedirectView.as_view(url='catalogue/', permanent=True), name='catalogue'),
]
