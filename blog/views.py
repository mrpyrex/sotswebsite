from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostCategory, Comment
from .forms import PostModelForm, PostCommentForm

# Create your views here.
class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostCatListView(ListView):
    model = Post
    template_name = 'blog/post_cat.html'


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'title': 'Blog Details',
        'post': post
        }
    return render(request, 'blog/post_detail.html', context)

    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_commment = comment_form.save(commit=False)
            new_commment.post = post
            new_commment.save()

    else:
        comment_form = PostCommentForm

    context = {
        'title': 'Blog Details',
        'post': post,
        'comments': comments
        }
    return render(request, 'blog/post_detail.html', context)


# class PostDetailView(DetailView):
#     model = Post

    # comments = post.comments.filter(active=True)
    # if request.method == 'POST':
    #     comment_form = PostCommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         new_commment = comment_form.save(commit=False)
    #         new_commment.post = post
    #         new_commment.save()

    # else:
    #     comment_form = PostCommentForm

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    template_name = 'blog/post_create.html'
    queryset = Post.objects.all()
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('blog:blog-home')
        


