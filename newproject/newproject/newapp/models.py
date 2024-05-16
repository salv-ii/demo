from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=256)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class games(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    type=models.CharField(max_length=250)

    def __str__(self):
        return self.name