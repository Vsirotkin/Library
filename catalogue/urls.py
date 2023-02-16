from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'catalogue'
urlpatterns = [
    path('', views.index, name='index'),
    # path('', RedirectView.as_view(url='catalogue/', permanent=True), name='catalogue'),
]
