from django.urls import path
from .views import (PostListView, 
                    # PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView,
                    UserPostListView,
                    )
from . import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<slug:slug>/',views.details, name='post-detail'),
    path('<slug:slug>/share',views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/',PostListView.as_view(), name='post-list-by-tag'),
    # path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),  
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('category/<slug:slug>/', views.post_category, name='post_category'),
]
