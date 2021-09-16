from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Vedio(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    
class Contactus(models.Model):
    Name = models.CharField(max_length=400, null=False, blank=True)
    country = models.CharField(max_length=400, null=False, blank=True)
    subject = models.CharField(max_length=400, null=False, blank=True)
    message = models.TextField(null=False, blank=True)
    Your_email = models.EmailField(null=True, blank=True)
    mobile = models.CharField( null=False, blank=True,max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "Contactus: " + str(self.Name)
    
class Categoryblog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title   
    
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Categoryblog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    view_count = models.PositiveIntegerField(default=0)
    description = RichTextUploadingField(null=True, blank=True)  
    small_description=models.TextField(null=True, blank=True,default="")
    seo=models.TextField(null=True, blank=True,default="")
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    First_name=models.CharField(max_length=200)
    Last_name =models.CharField(max_length=200)
    Email=models.EmailField(null=True, blank=True)
    Comment=models.TextField(null=True, blank=True,default="")
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.First_name
class Reviews(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    text=models.TextField(null=True, blank=True,default="")
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name    
    
