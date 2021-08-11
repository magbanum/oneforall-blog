from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('tags', views.TagList.as_view(), name='tag_list'),
    path('tags/<slug>', views.TagDetail.as_view(), name='tag_detail'),
    path('create/', views.CreatePost.as_view(), name='create_post'),
    path('<author>/<slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:author>/<slug:slug>/edit', views.EditPost.as_view(), name='edit_post'),
    path('<slug:author>/<slug:slug>/delete', views.DeletePost.as_view(), name='delete_post'),
    

]