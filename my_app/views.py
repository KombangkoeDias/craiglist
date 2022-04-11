from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from .models import Search


# Create your views here.
def home(request):
    # render base.html
    return render(request, 'base.html')

def new_search(request):
    # get data from request
    search = request.POST['search']
    Search.objects.create(search=search)

    url = f'https://losangeles.craigslist.org/search/apa?query={quote_plus(search)}'
    min_price = request.POST.get('min_price', 0)
    max_price = request.POST.get('max_price', 0)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'my_app/new_search.html', context=stuff_for_frontend)

