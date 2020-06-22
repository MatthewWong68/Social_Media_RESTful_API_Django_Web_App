# Generated by Django 2.2.1 on 2019-08-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
                ('author_id', models.IntegerField()),
                ('author_name', models.CharField(max_length=255)),
            ],
        ),
    ]