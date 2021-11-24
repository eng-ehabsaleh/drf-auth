from django.shortcuts import render

from rest_framework import generics 
from .serializer import PostSerializer
from .models import Post 
# Create your views here.

class PostList(generics.ListCreateApiView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.object.all()
    serializer_class=PostSerializer    