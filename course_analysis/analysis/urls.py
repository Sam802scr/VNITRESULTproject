from django.urls import path
from .views import histogram_view

urlpatterns = [
    path('', histogram_view, name='histogram'),
]
