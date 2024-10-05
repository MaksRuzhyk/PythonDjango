from django.urls import path
from .views import index, home_page, add_post, post_detail, author_page,add_like

urlpatterns = [
    path('', index, name='index'),
    path('home', home_page,  name='home'),
    path('add_post', add_post, name='add_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('author/<int:pk>/', author_page, name='author_page'),
    path('add_like/<int:pk>/', add_like, name='add_like'),
]
