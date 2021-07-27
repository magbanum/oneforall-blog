
from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
import requests, os

# Create your views here.


def get_hashnode_blogs(page):
    # headers dict with Personal Access Token
    headers = {
        "Authorization": os.getenv('TOKEN')
    }
    # Queries created with GraphQL
    query = """{{
        storiesFeed(type: FEATURED, page: {}){{
        title
        author{{
            name
            username
        }}
        coverImage
        dateAdded
        slug
        }}
    }}""".format(page)
    response = requests.post(url="https://api.hashnode.com", json={'query': query}, headers=headers)
    if response.status_code == 200:
        if page < 2:
            return tuple(response.json()['data']['storiesFeed']) + get_hashnode_blogs(page+1)
        return tuple(response.json()['data']['storiesFeed'])
    else:
        raise Exception("Query failed to run by returning code of {}.".format(response.status_code))
    


def HashnodeView(request):
    posts = get_hashnode_blogs(1)
    # posts += [get_hashnode_blogs(i)['data']['storiesFeed'] for i in range(5)]
    # posts += get_hashnode_blogs()['data']['storiesFeed']
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/hashnode_posts.html', {'page_obj': page_obj})


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
