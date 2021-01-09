from django.shortcuts import render
from .models import Book
import requests

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def store(request):
    if request.method == "POST":
        book = Book.objects.get(id=request.POST.get('id'))
        book.buy_book()
    books = Book.objects.all()
    count = books.count()
    context = {
        'count': count,
        'books': books,
    }
    return render(request, 'store/store.html', context)

def new_book(request):
    data = {
        'method': request.method,
        'title': ''
    }
    if request.method == 'POST':
        data['title'] = request.POST.get('title')
        try:
            new_book = Book(
                title=data['title'], 
                author=request.POST.get('author'),
                description="Default text",
                price=19.99
            )
            new_book.save() 
        except e:
            data['error'] = str(e)

    return render(request, 'store/new_book.html', data)


def repos(request):
    response = requests.get('https://api.github.com/users/facebook/repos')
    repos = response.json()
    data = {
        'repos': repos 
    }
    print(data.keys())
    return render(request, 'store/repos.html', data)