from django import forms
from .models import Video, Audio, Image

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio_file']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image_file']