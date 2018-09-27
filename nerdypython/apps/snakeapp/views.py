"""Views for the snake app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'snakeapp/snake_home.html')
