from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('register', views.SignUpView.as_view(), name='register'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-details'),
    path('<int:id>/review', views.review, name='book-review'),

]
