from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author
from .forms import PostModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.template.defaultfilters import slugify


class PostListView(ListView):
    queryset = Post.objects.filter(hide=False)



class PostDetailView(DetailView):
    queryset = Post.objects.filter(hide=False)



class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostModelForm
    queryset = Post.objects.all()


    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        form.instance.author, created = Author.objects.get_or_create(user=self.request.user)
        form.instance.slug = slugify(form.cleaned_data['subject'])
        form.instance.publish_date = timezone.now
        return super().form_valid(form)



class PostUpdateView(UpdateView):
    template_name = 'blog/post_update.html'
    form_class = PostModelForm

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug, hide=False)

    def form_valid(self, form):
        form.instance.last_modify = timezone.now
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    template_name = 'blog/post_delete.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug, hide=False)

    def get_success_url(self):
        return '../../'
