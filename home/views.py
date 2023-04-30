from django.shortcuts import render


def index(request):
    """A view that renders the home page"""

    return render(request, 'home/index.html')
