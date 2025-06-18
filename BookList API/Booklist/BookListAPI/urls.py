from django.urls import path
from .import views

urlpatterns = [
    #path('book/',views.books)
    path('book/',views.BookList.as_view()),
    path('book/<int:pk>',views.Book.as_view())
]
