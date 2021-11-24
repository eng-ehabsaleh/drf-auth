from rest_framework import Serializer 
from .models import Post

class PostSerializer(Serializer.ModelSerializer):
    class Meta:
        models = Post
        fields=('id','auther','title','body','created_at','updated_at')