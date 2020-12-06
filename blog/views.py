from django.contrib.auth import get_user_model


from rest_framework import generics

from .models import Post
from .serializers import PostSerializer, UserSerializer
from . permissions import IsAuthorOrReadonly


class Postlist(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadonly,)

    serializer_class = PostSerializer

# AllowAny - any user, authenticated or not, has full access
# • IsAuthenticated - only authenticated, registered users have access
# • IsAdminUser - only admins/superusers have access
# • IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only
# authenticated users have write, edit, or delete privileges


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (IsAuthorOrReadonly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    # permission_classes = (IsAuthorOrReadonly,)

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    # permission_classes = (IsAuthorOrReadonly,)

    serializer_class = UserSerializer
