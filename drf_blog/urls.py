from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/comments/', PostCommentsViewSet.as_view({'get':'posts'}), name='post-comments'),
    path('comments/', PostCommentsViewSet.as_view({'post':'create', 'get':'list'}), name='post-comments'),
    path('comments/create/', PostCommentsViewSet.as_view({'post':'create', 'get':'list'}), name='post-comments'),
    path('comments/<int:pk>/', PostCommentsViewSet.as_view({'get':'retrieve'}), name='post-comments'),
    path('comments/<int:pk>/edit', PostCommentsViewSet.as_view({'put':'update','get':'retrieve'  }), name='post-comments'),
    path('comments/<int:pk>/delete', PostCommentsViewSet.as_view({'delete':'destroy', 'get':'retrieve'}), name='post-comments'),
]