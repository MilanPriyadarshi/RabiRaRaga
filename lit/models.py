from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Sahitya(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    decs=models.TextField(default="")
    # slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +'Written by  '+self.author

