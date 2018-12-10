from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date_posted').filter(featured=True)
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'pages/contact.html', context)