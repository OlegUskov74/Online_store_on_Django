from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import BlogForm
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"

    def get_queryset(self):
        """ Изменение набора данных модели """
        return Blog.objects.filter(sign_publication=True)


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_lict')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """  Увеличение счётчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.watch_count += 1
        self.object.save(update_fields=['watch_count'])
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_lict')
