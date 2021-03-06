# Generated by Django 3.2 on 2021-04-18 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%Y/%m/')),
                ('vedio_url', models.CharField(max_length=222)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=222)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(max_length=222)),
                ('camera_type', models.CharField(max_length=222)),
                ('name', models.CharField(max_length=222)),
                ('subs_count', models.CharField(max_length=222)),
                ('is_feature', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=222)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
