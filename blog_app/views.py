from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from blog_app.models import Post


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog_app/detail.html'

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        return queryset.filter(status='published')


class PostListView(ListView):
    queryset = Post.published_ones.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/list.html'
