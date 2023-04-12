from django.shortcuts import render
from .models import Watch

# Create your views here.


def all_watches(request):
    """A view to show all watches, including sorting and search queries"""

    watches = Watch.objects.all()

    context = {
        'watches': watches,
    }

    return render(request, 'shop/watches.html', context)
