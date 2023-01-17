from django.db import models

class Post(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateField(auto_now_add =True)
    modified_date = models.DateField(auto_now = True)
