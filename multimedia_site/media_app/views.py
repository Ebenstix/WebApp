from django.shortcuts import render, redirect
from .models import Video, Audio, Image
from .forms import VideoForm, AudioForm, ImageForm


def home(request):
    videos = Video.objects.all()
    audios = Audio.objects.all()
    images = Image.objects.all()
    return render(request, 'media_app/home.html', {'videos': videos, 'images': images, 'audios': audios})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'media_app/upload_video.html', {'form': form})
    
def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AudioForm()
    return render(request, 'media_app/upload_audio.html', {'form': form})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'media_app/upload_image.html', {'form': form})
    
    