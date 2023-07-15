from django.db import models

class ImageDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    views = models.IntegerField()
    downloads = models.IntegerField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    user = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    previewURL = models.CharField(max_length=200)
    webformatURL = models.CharField(max_length=200)
