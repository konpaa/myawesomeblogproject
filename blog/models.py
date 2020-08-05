from django.db import models


# Create your models here.
class Post(models.Model):
	post_title=models.CharField(max_length=300)
	post_image=models.ImageField(upload_to='event_images/')
	post_text=models.TextField()
	post_data=models.DateTimeField()
