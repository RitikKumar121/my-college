from django.db import models

# Create your models here.

class Image(models.Model):
    #date=models.DateField(null=True)
    #datetime = models.DateTimeField(auto_now=True)
    caption=models.CharField(max_length=50)
    image=models.FileField(null=True)

    def __str__(self):
        return self.caption
