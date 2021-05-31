
from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
import requests

# Create your views here.
def get_news():
    resp = requests.get(url='https://newsapi.org/v2/top-headlines?country=in&apiKey=5e48c09225bd4247a0e0695857412b09')
    result = resp.json()
    blogs = result['articles']
    return blogs
def newsview(request):
    blogs = get_news()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/news_posts.html',{'page_obj': page_obj})

class HomeView(ListView):
    paginate_by = 6
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'

class EditView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit_post.html'
    # fields = ['title', 'body']
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

class MyPostsView(ListView):
    model = Post
    template_name = 'blog/dashboard.html'
    ordering = ['-post_date']
    