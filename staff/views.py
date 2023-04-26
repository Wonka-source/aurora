from django.shortcuts import render


def enquiry(request):
    """A view that renders the watch repair enquiry page"""

    form = WatchRepairForm()

    context = {'form': form}

    return render(request, 'watch_repair/repairs.html', context)
