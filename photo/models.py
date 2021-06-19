from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Photo(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    cameraman=models.CharField(max_length=100)
    decs=models.TextField(default="")
    # slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    image=models.ImageField(upload_to="photo/images",default="")

    def __str__(self):
        return self.title +'Captured by  '+self.cameraman

