from django.shortcuts import render, get_object_or_404
from .models import Watch

# Create your views here.


def all_watches(request):
    """A view to show all watches, including sorting and search queries"""

    watches = Watch.objects.all()

    context = {
        'watches': watches,
    }

    return render(request, 'shop/shop.html', context)


def watch_detail(request, watch_id):
    """A view to show individual watch details"""

    watch = get_object_or_404(Watch, pk=watch_id)

    context = {
        'watch': watch,
    }

    return render(request, 'shop/watch_detail.html', context)
