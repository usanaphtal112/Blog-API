from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .permissions import IsAuthororReadOnly

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthororReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthororReadOnly,)  # NEW
    queryset = Post.objects.all()
    serializer_class = PostSerializer
