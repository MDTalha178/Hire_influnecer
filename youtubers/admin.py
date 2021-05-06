from django.contrib import admin
from django.contrib.admin.decorators import register
from .models  import Youtuber
from django.utils.html import format_html

# Register your models here.
class YtAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    list_display = ('id', 'name', 'myphoto','subs_count', 'is_feature')
    search_feilds = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('name','id')
    list_editable =('is_feature',)
admin.site.register(Youtuber,YtAdmin)
