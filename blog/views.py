from django.contrib.auth.models import User
from django.urls.base import reverse, reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from blog.forms import  PostForm
from blog.models import Post, Tag
from django.views.generic import ListView, DetailView,CreateView


# Create your views here.
class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'
    paginate_by = 5

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    

class TagList(ListView):
    queryset = Tag.objects.all()
    template_name = 'blog/tag_list.html'

class TagDetail(DetailView):
    model = Tag
    slug_field = 'title'
    context_object_name = 'tag'
    template_name = 'blog/tag_detail.html'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

    def get_success_url(self):
        return reverse('post_detail', args=(self.object.author, self.object.slug))
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'

    def get_success_url(self):
        return reverse('post_detail', args=(self.object.author, self.object.slug))
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

