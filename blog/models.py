from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from embed_video.fields  import  EmbedVideoField
# Create your models here.

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image_header = CloudinaryField('image', null=True,blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    content = RichTextField()
    post_Video = EmbedVideoField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)
    

    # class Image(models.Model):
    #     imagetitle = models.CharField(max_length=200)
    #     image = CloudinaryField('image')

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

class PolicyPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = RichTextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)

    def __str__(self):
        return self.title
    
