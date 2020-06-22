from rest_framework import serializers
from .models import Post, Hashtag, Page
# from .models import PostHistory

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=31)
    full_text = serializers.CharField(max_length=8191)
    author_name = serializers.CharField(max_length=255)
    crawled_dt = serializers.DateTimeField()
    post_dt = serializers.DateTimeField()
    like = serializers.IntegerField(default=0)
    comment = serializers.IntegerField(default=0)

    # Create <=> POST
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    # Update <=> PUT
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.full_text = validated_data.get('full_text', instance.full_text)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.crawled_dt = validated_data.get('crawled_dt', instance.crawled_dt)
        instance.post_dt = validated_data.get('post_dt', instance.post_dt)
        instance.like = validated_data.get('like', instance.like)
        instance.comment = validated_data.get('comment', instance.comment)

        instance.save()
        return instance

class HashtagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    feedID = serializers.CharField(max_length=20)
    text = serializers.CharField(max_length=255)

    # Create <=> POST
    def create(self, validated_data):
        return Hashtag.objects.create(**validated_data)

    # Update <=> PUT
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.feedID = validated_data.get('feedID', instance.feedID)
        instance.text = validated_data.get('text', instance.text)

        instance.save()
        return instance

class PageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author_name = serializers.CharField(max_length=255)
    posts = serializers.IntegerField(default=0)
    followers = serializers.IntegerField(default=0)
    following = serializers.IntegerField(default=0)

    # Create <=> POST
    def create(self, validated_data):
        return Page.objects.create(**validated_data)

    # Update <=> PUT
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.posts = validated_data.get('posts', instance.posts)
        instance.followers = validated_data.get('followers', instance.followers)
        instance.following = validated_data.get('following', instance.following)
        
        instance.save()
        return instance

# class PostHistorySerializer(serializers.Serializer):
#     # Create <=> POST
#     def create(self, validated_data):
#         return PostHistory.objects.create(**validated_data)