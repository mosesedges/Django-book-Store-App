from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

# bookData = open('buyer_site\EmployeeData.json').read()
# data = json.loads(bookData)


class BookListView(ListView):
    model = Book
    # template_name = "buyer_site/index.html"
    # context_object_name = 'data'
    # def get_queryset(self):
    #     return Book.objects.all()

# def index(request):
#     data = Book.objects.all()
#     context = {'data': data}
#     return render(request, 'buyer_site/index.html', context)


# def book_author(request, author):
#     books = Book.objects.filter(authors__name=author)
#     context = {'books': books}
#     return render(request, 'buyer_site/book_list.html', context)


class BookDetailView(DetailView):
    model = Book


# def book_details(request, id):
#     details = get_list_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id)
#     context = {'details': details, 'reviews': reviews}
#     return render(request, 'buyer_site/book_details.html', context)

def review(request, id):
    if request.user.is_authenticated:
        body = request.POST['review']
        NewReviews = Review(body=body, book_id=id, user=request.user)
        NewReviews.save()
    return redirect('/buyer_site')
