from django.shortcuts import render

def index(request):
    """ A view returning to home page """

    return render(request, 'home/index.html')