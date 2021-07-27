from typing import Pattern
from django.urls import path
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
import blog.views
from .views import AddPostView, EditView, HomeView, ArticleDetailView, DeletePostView, MyPostsView

urlpatterns = [
    path('hashnode-latest-posts/', blog.views.HashnodeView, name='hashnode_posts'),
    path('', HomeView.as_view(), name="home"),
    path('articles/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('articles/edit/<int:pk>', EditView.as_view(), name='edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('dashboard/',MyPostsView.as_view(), name='user_posts'),
]
