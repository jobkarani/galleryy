from django.http  import HttpResponse, Http404
from django.shortcuts import render,redirect
import datetime as dt

from pic.models import Image,Category,Location

# Create your views here.
def index(request):
    img = Image.objects.all()
    cat = Category.objects.all()
    loc = Location.objects.all()

    if 'cat' in request.GET and request.GET["cat"]:
      cat_id = request.GET.get("cat")
      img = Image.objects.filter(cat = cat_id)
    else:
      img = Image.objects.all()

    if 'loc' in request.GET and request.GET["loc"]:
      loc_id = request.GET.get("loc")
      img = Image.objects.filter(loc = loc_id)
    else:
      img = Image.objects.all()

    return render(request, 'all-pics/index.html',{'img':img,'cat':cat,'loc':loc})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Image.search_by_category(search_term)
        message = search_term

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

    