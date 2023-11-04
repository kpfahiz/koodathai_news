from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField
#from tinymce import HTMLField
from tinymce import models as tinymce_models

User =get_user_model()



class PostView(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    ads_img = CloudinaryField('image')

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post',related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class Author(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = CloudinaryField('image')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)


    def __str__(self):
        return self.title



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(max_length=100)
    overview = models.TextField()
    content = tinymce_models.HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default=0)
    #view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = CloudinaryField('image')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self',related_name='previous',on_delete=models.SET_NULL,blank=True,null=True)
    next_post = models.ForeignKey('self',related_name='next',on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.title

    def get_absalute_url(self):
        return reverse('post_details',kwargs={
            'id':self.id,
        })
    def get_update_url(self):
        return reverse('post_update',kwargs={
            'id':self.id,
        })
    def get_delete_url(self):
        return reverse('post_delete',kwargs={
            'id':self.id,
        })
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()




