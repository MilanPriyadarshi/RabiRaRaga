from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class StatePost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    author=models.CharField(max_length=100)
    # slug=models.CharField(max_length=130)
    views=models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    image=models.ImageField(upload_to="state/images",default="")

    def __str__(self):
        return self.title +'Post from '+self.author 