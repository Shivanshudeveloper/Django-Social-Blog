from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
)

urlpatterns= [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>/', UserPostListView, name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    # post_form.html will be created in the template forlder
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about")
]