from django.shortcuts import render

from books.models import Book, Genre


def home(request):
    return render(request, 'home.html')


def search_manga(request):
    if request.method == "POST":
        searched = request.POST[('searched')]
        mangas = Book.objects.filter(title__contains=searched)
        return render(request, 'books/search_manga.html', {'searched': searched, 'mangas': mangas})
    else:
        return render(request, 'books/search_manga.html', {})
