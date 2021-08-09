from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.urls.base import reverse_lazy
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import markdown # pip install markdown
from bs4 import BeautifulSoup # pip install beautifulsoup4

POST_STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

# To convert Markdown to Plain text
def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

# non_url_safe = ['"', '#', '$', '%', '&', '+',
#                     ',', '/', ':', ';', '=', '?',
#                     '@', '[', '\\', ']', '^', '`',
#                     '{', '|', '}', '~', "'"]

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_list')

class Post(models.Model):
    # def slugify(self, text):
        
    #     non_safe = [c for c in text if c in non_url_safe]
    #     if non_safe:
    #         for c in non_safe:
    #             text = text.replace(c, '')
    #     text = u'-'.join(text.split())
    #     return text
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = MarkdownxField()
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug 
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('post_detail', args=(self.author, self.slug))

    def formatted_markdown(self):
        return markdownify(self.content)

    def body_summary(self):
        return md_to_text(self.content[:200] + "...")

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self.slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)