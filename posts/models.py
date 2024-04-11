from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
     
