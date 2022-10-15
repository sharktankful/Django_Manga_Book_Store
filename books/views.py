from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

import books
from . models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def detail(request, book_id):   
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/detail.html", {'book': book})

