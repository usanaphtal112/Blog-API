from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# # Beloow two classes uses viewsets to perform all works perfomed previously by the above 4 views classes
# class PostViewSet(viewsets.ModelViewSet):  # new
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet):  # new
#     permission_classes = [IsAdminUser]  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
