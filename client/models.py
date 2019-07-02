from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ORDER_STATUS = ((0, 'Close'), (1, 'Open'))

class Slide(models.Model):

    title  =    models.TextField(null=True)
    image   =   models.ImageField()
    date    =   models.DateTimeField(auto_now_add =True)
    status  =   models.PositiveSmallIntegerField(choices=ORDER_STATUS)



class New(models.Model):

    title           =    models.CharField(max_length=255)
    content         =    models.TextField(null=True)
    image           =     models.ImageField(null=True)
    content_fast    =     models.CharField(max_length=255,null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    created_by      = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        self.path = self.title.replace(' ','-')
        return self.path
    

class Comment(models.Model):
    name            = models.CharField(max_length=100,default="Người vô danh")
    content         = models.TextField()
    sub_comment     = models.IntegerField(default=0)
    image           = models.ImageField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    new_id          = models.ForeignKey(New,on_delete=models.CASCADE, related_name='comments')


