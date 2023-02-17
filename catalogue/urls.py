from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'catalogue'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # path('', RedirectView.as_view(url='catalogue/', permanent=True), name='catalogue'),
]
