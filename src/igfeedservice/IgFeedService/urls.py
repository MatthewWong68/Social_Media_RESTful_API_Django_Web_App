from django.urls import path
from rest_framework import renderers

from .views import PostViewSet, HashtagViewSet, PageViewSet
# from .views import PostHistoryViewSet

# app_name will help us do a reverse look-up latter.
app_name = "posts"
app_name = "hashtags"
app_name = "pages"
# app_name = "postshistory"

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

hashtag_list = HashtagViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
hashtag_detail = HashtagViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

page_list = PageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
page_detail = PageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# posthistory_list = PostHistoryViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# posthistory_detail = PostHistoryViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

urlpatterns = [
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('hashtags/', hashtag_list, name='hashtag-list'),
    path('hashtags/<int:pk>/', hashtag_detail, name='hashtag-detail'),
    path('pages/', page_list, name='page-list'),
    path('pages/<int:pk>', page_detail, name='page-detial')
    # path('posthistory/', posthistory_list, name='posthistory-list'),
    # path('posthistory/<int:pk>', posthistory_detail, name='posthistory-detial')
]