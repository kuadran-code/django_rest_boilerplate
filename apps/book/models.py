import os
from django.db import models



def get_upload_path(instance, filename):
    return os.path.join("book", "%d" % instance.id, filename)

# Create your models here.
class Book(models.Model):
    name = models.CharField()
    description = models.CharField()
    cover = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
