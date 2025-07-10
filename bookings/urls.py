from django.urls import path
from .views import book_class

urlpatterns = [
    path('book/', book_class, name='book_class'),
]
