from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    upload_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Audio(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    upload_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.FileField(upload_to='images/')
    upload_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
