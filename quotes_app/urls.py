from django.urls import path
from .views import register, add_author, add_quote, author_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
    ]