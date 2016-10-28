from django.db import models

# Create your models here.

#General topic that handles topics to be used by the users
class Course(models.Model):

    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.CharField(max_length=500, unique=True)
    thumbnailUrl = models.CharField(max_length=500)
    level = models.CharField(max_length=200, blank=True)

    #url = models.URLField(unique=True)
    #pageid = models.BigIntegerField(unique=True)
    #urlTitle = models.CharField(max_length=200, unique=True)
    #language = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
