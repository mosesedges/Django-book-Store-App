from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# bookData = open('buyer_site\EmployeeData.json').read()
# data = json.loads(bookData)


class BookListView(ListView):
    paginate_by = 4
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get('book_search')
        if query != '' and query is not None:
            object_list = self.model.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query))
        else:
            object_list = self.model.objects.all()
        return object_list

    # template_name = "buyer_site/index.html"
    # context_object_name = 'data'
    # def get_queryset(self):
    #     return Book.objects.all()


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
    return redirect(f"/buyer_site/{id}")


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
