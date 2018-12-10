from django.urls import path
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView,
                    UserPostListView,
                    PostCatListView,
                    )
from . import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),  
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
