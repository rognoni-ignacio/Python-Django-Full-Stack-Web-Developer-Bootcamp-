from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog_app.models import Post
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'