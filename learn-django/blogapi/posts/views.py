# @Author: @IamRezaMousavi
# @Date:   2023-02-14 19:05:18
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 19:43:55
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
