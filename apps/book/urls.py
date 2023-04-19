from django.urls import path

from .views import BookDetail, BookList


urlpatterns = [
    path('book/', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail')
]
