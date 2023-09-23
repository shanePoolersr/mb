from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView
    ) 
from django.views.generic.edit import DeleteView
from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
class PostDetailView(DetailView):
    template_name = "posts/deatail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
        model = Post

class PostUpdateView(UpdateView):
        model = Post
