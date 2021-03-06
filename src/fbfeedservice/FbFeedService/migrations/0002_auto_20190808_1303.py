# Generated by Django 2.2.1 on 2019-08-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FbFeedService', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='link',
            new_name='full_text',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='created_time',
            new_name='post_dt',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='name',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='updated_time',
        ),
        migrations.AddField(
            model_name='feed',
            name='angry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='haha',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='love',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='reactions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='sad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='wow',
            field=models.IntegerField(default=0),
        ),
    ]
