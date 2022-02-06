from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,CommentCreateView,LatestPostsListView,TopCommentsListView #AddCommentView


urlpatterns = [
    #path('',views.home,name='blog-blog'),
    path('', PostListView.as_view(),name='blog-home'),
    path('latestposts/',LatestPostsListView,name='latest-posts'),
    path('topcomments/',TopCommentsListView,name='top-comments'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    #path('post/<int:pk>/',PostDetailView.as_view(),name='post-details'),
    path('post/<int:pk>/',PostDetailView,name='post-details'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/comment/',CommentCreateView.as_view(),name='add-comment'),
]
