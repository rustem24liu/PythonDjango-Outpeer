from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response

from drf_blog.models import Post, Comment
from drf_blog.serializers import PostSerializer, CommentSerializer
from .permissions import *


# Create your views here.


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = ()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly]


class PostDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly]


class PostCommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def posts(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        comment = post.comments.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
