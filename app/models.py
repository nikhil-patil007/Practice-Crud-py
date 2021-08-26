from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=255,default='abc')
    username = models.CharField(max_length=255,default='abc@012')
    email = models.EmailField(unique=True)
    Image = models.ImageField(upload_to="images/",default="abc.jpg")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name