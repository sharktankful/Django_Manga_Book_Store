from django.urls import path
from . import views


# books/
# books/1/details

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>', views.detail, name='detail')
]