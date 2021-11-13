from . import views
from django.urls import path

#  path('register', views.SignUpView.as_view(), name='register'),


urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-details'),
    path('<int:id>/review', views.review, name='book-review'),

]
