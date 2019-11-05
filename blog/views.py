from django.shortcuts import render
from django.http import HttpResponse
# Importing the Model for database model Post
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
# For Not Accessing the url from the url address bar
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Home Funcstion for the home page
def home(request):
    # Create a distonary
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# For listing the all the post
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # By Default it looks into <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # Odering from the latest post on date
    ordering = ['-date_posted']


# For Detail View of  Post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


# For Create Post
# LoginRequiredMixin Added for the Login URL Access block from the url address bar
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # For the author we have to overwrite the form valid method
    #
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# For Delete View of  Post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# For Update Post
# LoginRequiredMixin Added for the Login URL Access block from the url address bar
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # For the author we have to overwrite the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

# About Function for the about Page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})