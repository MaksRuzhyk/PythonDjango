from django.urls import path
from .views import index, home_page, add_post, post_detail, author_page, add_like, post_edit, UserLogin, UserLogout

urlpatterns = [
    path('', index, name='index'),
    path('home',home_page, name='home'),
    path('add_post',add_post,name='add_post'),
    path('post/<int:pk>/',post_detail,name='post_detail'),
    path('author/<int:pk>/',author_page,name='author_page'),
    path('add_like/<int:pk>/',add_like,name='add_like'),
    path('post_edit/<int:pk>/',post_edit,name='post_edit'),
    path('accounts/login/',UserLogin.as_view(),name='login'),
    path('accounts/logout/',UserLogout.as_view(),name='logout'),
    ]
