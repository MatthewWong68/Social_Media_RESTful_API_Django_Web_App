from rest_framework import serializers
from .models import Feed, Hashtag, Page, IGPost

class FeedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_text = serializers.CharField(max_length=8191)
    crawled_dt = serializers.DateTimeField()
    post_dt = serializers.DateTimeField()
    author_name = serializers.CharField(max_length=255)
    reactions = serializers.IntegerField(default=0)
    like = serializers.IntegerField(default=0)
    love = serializers.IntegerField(default=0)
    angry = serializers.IntegerField(default=0)
    wow = serializers.IntegerField(default=0)
    haha = serializers.IntegerField(default=0)
    sad = serializers.IntegerField(default=0)
    comment = serializers.IntegerField(default=0)
    share_count = serializers.IntegerField(default=0)
    # hashtags = serializers.CharField(max_length=8191)

    # Create <=> POST
    def create(self, validated_data):
        return Feed.objects.create(**validated_data)

    # Update <=> PUT
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.full_text = validated_data.get('full_text', instance.full_text)
        instance.crawled_dt = validated_data.get('crawled_dt', instance.crawled_dt)
        instance.post_dt = validated_data.get('post_dt', instance.post_dt)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.reactions = validated_data.get('reactions', instance.reactions)
        instance.like = validated_data.get('like', instance.like)
        instance.love = validated_data.get('love', instance.love)
        instance.angry = validated_data.get('angry', instance.angry)
        instance.wow = validated_data.get('wow', instance.wow)
        instance.haha = validated_data.get('haha', instance.haha)
        instance.sad = validated_data.get('sad', instance.sad)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.share_count = validated_data.get('share_count', instance.share_count)

        instance.save()
        return instance

class HashtagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField(max_length=255)
    feedID = serializers.IntegerField()

    # Create <=> POST
    def create(self, validated_data):
        return Hashtag.objects.create(**validated_data)

    # Update <=> PUT
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.text = validated_data.get('text', instance.text)
        # instance.crawled_dt = validated_data.get('crawled_dt', instance.crawled_dt)
        instance.feedID = validated_data.get('feedID', instance.feedID)
        
        instance.save()
        return instance

class PageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author_name = serializers.CharField(max_length=255)
    ads = serializers.BooleanField()
    page_created_date = serializers.DateField()
    total_number_of_manager = serializers.IntegerField(default=0)
    manager = serializers.CharField(max_length=511)

    # Create <=> POST
    def create(self, validated_data):
        return Page.objects.create(**validated_data)

    # Update <=> PUT
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.ads = validated_data.get('ads', instance.ads)
        instance.page_created_date = validated_data.get('page_created_date', instance.page_created_date)
        instance.total_number_of_manager = validated_data.get('total_number_of_manager', instance.total_number_of_manager)
        instance.manager = validated_data.get('manager', instance.manager)
        
        instance.save()
        return instance
