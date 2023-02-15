from django.urls import path
from django.views.generic import RedirectView

app_name = 'catalogue'
urlpatterns = [
    path('', RedirectView.as_view(url='catalogue/', permanent=True), name='catalogue'),
]
