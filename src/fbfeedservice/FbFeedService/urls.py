from django.urls import path
from rest_framework import renderers

from .views import FeedViewSet, HashtagViewSet, PageViewSet

# app_name will help us do a reverse look-up latter.
app_name = "feeds"
app_name = "hashtags"
app_name = "pages"

feed_list = FeedViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
feed_detail = FeedViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
feed_highlight = FeedViewSet.as_view({
    'get': 'highlight'
})#, renderer_classes=[renderers.StaticHTMLRenderer])

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

urlpatterns = [
    path('feeds/', feed_list, name='feed-list'),
    path('feeds/<int:pk>/', feed_detail, name='feed-detail'),
    path('feeds/<int:pk>/highlight/', feed_highlight, name='feed-highlight'),
    path('hashtags/', hashtag_list, name='hashtag-list'),
    path('hashtags/<int:pk>/', hashtag_detail, name='hashtag-detail'),
    path('pages/', page_list, name='page-list'),
    path('pages/<int:pk>', page_detail, name='page-detial')
]

# urlpatterns = format_suffix_patterns([
#     path('feeds/', feed_list, name='feed-list'),
#     path('feeds/<int:pk>/', feed_detail, name='feed-detail'),
#     path('feeds/<int:pk>/highlight/', feed_highlight, name='feed-highlight')
# ])

# urlpatterns = [
#     path('feeds/<int:id>', FeedView.as_view()),
#     # path('feeds/<int:id>', FeedView.as_view({'post':'create'})),
#     # path('feeds/<int:id>', FeedView.as_view({'put':'update'})),
#     # path('feeds/', FeedView.as_view({'get':'list'})),
#     path('feeds/', FeedView.as_view())
# ]