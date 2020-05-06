from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date =models.DateField('date published')
    body = models.TextField()
    image = models.ImageField( upload_to='images/')