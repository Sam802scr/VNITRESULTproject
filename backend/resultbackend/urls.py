from django.urls import path
from . import views

urlpatterns = [
    path('grade-distribution/', views.get_grade_distribution, name='grade_distribution'),
]
