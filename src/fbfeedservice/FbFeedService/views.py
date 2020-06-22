# from django.shortcuts import render, redirect
# from django.shortcuts import get_list_or_404, get_object_or_404

# article_get_view.py
from rest_framework import status, viewsets, renderers
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import action
# from rest_framework.reverse import reverse

from .models import Feed, Hashtag, Page, IGPost
from .serializers import FeedSerializer, HashtagSerializer, PageSerializer, IGPostSerializer

class FeedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]

    def create(self, request):
        """overide default create() method of ModelViewSet, supporting Create-or-Update pattern
        
        Arguments:
            request {Request} -- HTTP Request
        
        Returns:
            Response -- Response with Json object
        """
        resultFeed, created = Feed.objects.update_or_create(
            id = request.data.get('id'),
            defaults = request.data)
        serializer = FeedSerializer(resultFeed, many=False)
#ToDo 1: Remove all HashtagFeed rows for this feed
#ToDo 2: Add all Hashtag for this feed back

        return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 
        # '[value_when_true] if [True/False] else [value_when_false]' is Python's ternary operator expression for one-line condition result. 
        # See https://stackoverflow.com/a/2802748/4684232

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        # feed = self.get_object()
        return Response({"result":"OK"})

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class HashtagViewSet(viewsets.ModelViewSet):
    
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]

    def create(self, request):
        
        resultHashtag, created = Hashtag.objects.update_or_create(
            id = request.data.get('id'),
            defaults = request.data)
        serializer = HashtagSerializer(resultHashtag, many=False)
#ToDo 1: Remove all HashtagFeed rows for this feed
#ToDo 2: Add all Hashtag for this feed back

        return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 

class PageViewSet(viewsets.ModelViewSet):
    
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]

    def create(self, request):
        
        resultPage, created = Page.objects.update_or_create(
            id = request.data.get('id'),
            defaults = request.data)
        serializer = PageSerializer(resultPage, many=False)

        return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 