from django.views.generic import ListView, DetailView

from blog.models import Category, Post


class BlogView(ListView):
    model = Category
    template_name = 'blog/main.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Blog'}


class CategoryView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = context['posts'][0].category
        return context


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
