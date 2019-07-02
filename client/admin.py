from django.contrib import admin
from .models import *

# Register your models here.


class SlideAdmin(admin.ModelAdmin):
    list_display    =['status','image','date']
    search_fields   =['status']
    list_filter     =['status']


admin.site.register(Slide,SlideAdmin)



class NewsAdmin(admin.ModelAdmin):
    list_display    =['status','title','created_by','created_at','updated_at']
    search_fields   =['title']
    list_filter     =['status']


admin.site.register(New,NewsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display    =['new_id','name','created_at']
    search_fields   =['new_id']
    list_filter     =['new_id']


admin.site.register(Comment,CommentAdmin)