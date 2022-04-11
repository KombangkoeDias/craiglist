from cgitb import text
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from .models import Search
import requests
import re


# Create your views here.
def home(request):
    # render base.html
    return render(request, 'base.html')

def new_search(request):
    # get data from request
    search = request.POST['search']
    Search.objects.create(search=search)
    url = 'https://losangeles.craigslist.org/search/sss?query={}'
    final_url = url.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    print(post_listings[0])
    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'
            
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0][2:]
            post_image_url = 'https://images.craigslist.org/{}_300x300.jpg'.format(post_image_id)
        else:
            post_image_url = 'https://images.craigslist.org/images/peace.jpg'
        
        final_postings.append((post_title, post_url, post_price, post_image_url))

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings
    }
    return render(request, 'my_app/new_search.html', context=stuff_for_frontend)

