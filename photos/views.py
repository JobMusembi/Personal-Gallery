from django.shortcuts  import render
from .models import Image

# Create your views here.
def welcome(request):
    photos = Image.photos_display()
    return render(request, 'landing.html',{"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def filter_results(request):

    if 'location' in request.GET and request.GET["location"]:
        location_term = request.GET.get("location")
        searched_location = Image.filter_by_location(location_term)
        message = f"{location_term}"

        return render(request, 'location.html',{"message":message,"locations": searched_location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'location.html',{"message":message})
