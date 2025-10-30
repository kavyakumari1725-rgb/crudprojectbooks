"""bookstore.views

Function-based Django views for CRUD operations on the Book model.

Provides:
- book_list(request): list all books -> template 'book_list.html' (context: 'books')
- book_create(request): create a new book -> template 'book_form.html' (context: 'form')
- book_update(request, pk): edit an existing book -> template 'book_form.html' (context: 'form')
- book_delete(request, pk): confirm and delete -> template 'book_confirm_delete.html' (context: 'book')

Notes:
- Templates should include {% csrf_token %} for POST forms.
- Redirects assume a URL pattern named 'book_list'.
- Consider adding authentication, messages, or switching to class-based generic views if desired.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
