from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):
    crew_choices = (
        ('solo', 'solo'),
        ('small' , 'small'),
        ('large', 'large'),
    )
    camera_choice = (
        ('canon', 'canon'),
        ('nikon' , 'nikon'),
        ('sony', 'sony'),
        ('red', 'red'),
        ('fuji' , 'fuji'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    )
    category_choice = (
        ('codeer', 'coder'),
        ('mobile_review' , 'mobile_review'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('gaming' , 'gaming'),
        ('film_making', 'film_making'),
        ('cooking', 'cooking'),
    )
    name = models.CharField(max_length=222)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    vedio_url = models.CharField(max_length=222)
    description = RichTextField()
    city = models.CharField(max_length=222)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices ,max_length=222)
    camera_type = models.CharField(choices=camera_choice,max_length=222)
    name = models.CharField(max_length=222)
    subs_count = models.CharField(max_length=222)
    is_feature = models.BooleanField(default=False)
    category = models.CharField(choices=category_choice, max_length=222)
    created_date = models.DateTimeField(default=datetime.now,blank=True)