from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']

        Book.objects.create(
            title=title,
            author=author,
            description=description,
            owner=request.user
        )
        return redirect('book_list')

    return render(request, 'books/book_form.html')


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.user != book.owner:
        return redirect('book_list')

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.save()
        return redirect('book_list')

    return render(request, 'books/book_form.html', {'book': book})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.user == book.owner:
        book.delete()

    return redirect('book_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # connecte automatiquement l'utilisateur
            return redirect('book_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})