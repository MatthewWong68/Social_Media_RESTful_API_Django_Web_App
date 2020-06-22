from rest_framework import status, viewsets, renderers
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import render

from .models import Page, Post, Hashtag
# from .models import PostHistory
from .serializers import HashtagSerializer, PageSerializer, PostSerializer
# from .serializers import PostHistorySerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request):
        resultPost, created = Post.objects.update_or_create(
            id = request.data.get('id'),
            defaults = request.data)
        serializer = PostSerializer(resultPost, many=False)

        return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 

    def highlight(self, request, *args, **kwargs):
        return Response({"result":"OK"})

# class PostHistoryViewSet(viewsets.ModelViewSet):
#     serializer_class = PostHistorySerializer
#     queryset = PostHistory.objects.all()

    # def create(self, request):
    #     resultPost, created = Post.objects.update_or_create(
    #         id = request.data.get('id'),
    #         defaults = request.data)
    #     serializer = PostSerializer(resultPost, many=False)

    #     return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 

    # def highlight(self, request, *args, **kwargs):
    #     return Response({"result":"OK"})

class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()

    def create(self, request):
        resultPage, created = Page.objects.update_or_create(
            id = request.data.get('id'),
            defaults = request.data)
        serializer = PageSerializer(resultPage, many=False)

        return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 

    def highlight(self, request, *args, **kwargs):
        return Response({"result":"OK"})

class HashtagViewSet(viewsets.ModelViewSet):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()

    def create(self, request):
        resultHashtag, created = Hashtag.objects.update_or_create(
            id = request.data.get('id'),
            defaults = request.data)
        serializer = HashtagSerializer(resultHashtag, many=False)

        return Response(serializer.data, status = status.HTTP_201_CREATED if created else status.HTTP_200_OK) 

    def highlight(self, request, *args, **kwargs):
        return Response({"result":"OK"})