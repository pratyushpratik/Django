from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=200)
    albumTitle = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    albumLogo = models.CharField(max_length=200)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=50)

