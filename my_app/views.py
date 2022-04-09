from django.shortcuts import render

# Create your views here.
def home(request):
    # render base.html
    return render(request, 'base.html')

