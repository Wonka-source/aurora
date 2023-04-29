from django.shortcuts import render
from .forms import WatchRepairForm
# Create your views here.


def enquiry(request):
    """A view that renders the watch repair enquiry page"""

    form = WatchRepairForm()

    context = {'form': form}

    return render(request, 'watch_repair/repairs.html', context)
