from pathlib import PosixPath
from django.shortcuts import render, redirect


def index(request):
    """A view that renders the home page"""

    return render(request, 'home/index.html')
