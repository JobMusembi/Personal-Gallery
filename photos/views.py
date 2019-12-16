from django.shortcuts  import render
from .models import Image

# Create your views here.
def welcome(request):
    photos = Image.photos_display()
    return render(request, 'landing.html',{"photos":photos})
