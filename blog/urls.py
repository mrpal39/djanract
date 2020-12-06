from django.urls import path
from .views import Postlist, PostDetail, UserList, UserDetail
urlpatterns = [

    path('<int:pk>/', PostDetail.as_view()),
    path('', Postlist.as_view()),

    path('users/', UserList.as_view()),  # new
    path('users/<int:pk>/', UserDetail.as_view()),  # new
]
