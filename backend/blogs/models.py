from distutils.command.upload import upload
from django.db import models
from django.contrib import admin
from django.conf import settings

from blogs.validators import validate_file_size

# Create your models here.


class Blogger(models.Model):
 BLOGGER_BRONZE = 'B'
 BLOGGER_SILVER = 'S'
 BLOGGER_GOLD = 'G'
 BLOGGER_CHOICES = [
        (BLOGGER_BRONZE, 'Bronze'),
        (BLOGGER_SILVER, 'Silver'),
        (BLOGGER_GOLD, 'Gold'),
    ]
 phone = models.CharField(max_length=255)
 birth_date = models.DateField(null=True, blank=True)
 membership = models.CharField(
         max_length=1, choices=BLOGGER_CHOICES, default=BLOGGER_BRONZE)
 user = models.OneToOneField(
         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


 def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
 

 @admin.display(ordering='user__first_name')
 def first_name(self):
        return self.user.first_name
  
 @admin.display(ordering='user__last_name')
 def last_name(self):
        return self.user.last_name
        
 class Meta:
  ordering = ['user__first_name', 'user__last_name']

class BloggersImage(models.Model):
       blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='images'  )
       image = models.ImageField(upload_to='bloggers/images', 
       validators=[validate_file_size])

class Posts(models.Model):
 blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
 description = models.TextField()
 date = models.DateField(auto_now_add=True)

class PostsImage(models.Model):
       post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='images'  )
       image = models.ImageField(upload_to='posts/images', 
       validators=[validate_file_size])