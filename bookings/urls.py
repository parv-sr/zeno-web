from django.urls import path
from .views import book_class, feedback_view

urlpatterns = [
    path('book/', book_class, name='book_class'),
    path('feedback/', feedback_view, name='feedback')
]
