from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/video/', views.upload_video, name="upload_video"),
    path('upload/audio/', views.upload_audio, name="upload_audio"),
    path('upload/image/', views.upload_image, name="upload_image"),
]