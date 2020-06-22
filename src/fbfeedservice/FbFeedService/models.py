from django.db import models

class Feed(models.Model):
    id = models.BigIntegerField(primary_key=True)
    full_text = models.CharField(max_length=8191)
    crawled_dt = models.DateTimeField(auto_now=False)
    post_dt = models.DateTimeField(auto_now=False)
    author_name = models.CharField(max_length=255)
    reactions = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    wow = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
  
    def __str__(self):
        return self.id
       
class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    feedID = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.id

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    ads = models.BooleanField(default=True)
    page_created_date = models.DateField(auto_now=False)
    total_number_of_manager = models.IntegerField(default=0)
    manager = models.CharField(max_length=511)
    
    def __str__(self):
        return self.id

# class FbUser(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=255)

# "id": "10155917661702853",
# "metadata": {
#     "type": "photo"
# },
# "created_time": "2017-11-03T20:59:48+0000",
# "link": "https://www.facebook.com/MarkRWarner/photos/a.490322322852.293145.7935122852/10155917661702853/?type=3",
# "name": "#GetCovered at healthcare.gov, now through December 15th.",
# "updated_time": "2017-11-18T01:13:33+0000",
# "from": {
#     "name": "Senator Mark Warner",
#     "id": "7935122852"
# },
# "height": 360,