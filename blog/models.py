from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
   title = models.CharField(max_length=255)
   header_image = models.ImageField(null=True, blank=True, upload_to="images/")
   title_tag = models.CharField(max_length=255)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   post_date = models.DateField(auto_now_add=True)
   # body = models.TextField()
   body = RichTextField(blank='True', null='True')

   def __str__(self):
      return self.title +' | '+ str(self.author)

   def get_absolute_url (self):
      # return reverse('article', args=(str(self.id)))
      return reverse('home')
