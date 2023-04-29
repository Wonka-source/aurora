from django.shortcuts import render, redirect
from .forms import WatchRepairForm
from django.contrib import messages
# Create your views here.


def enquiry(request):
    """A view that renders the watch repair enquiry page"""

    if request.method == 'POST':
        form = WatchRepairForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            messages.success(request, "Success. Your message has been submitted. We'll get back to you within 3 working days.")
            return redirect('shop')
        else:
            messages.error(request, 'Something went wrong! Please try again! If this continues please contact support.')
    else:    
        form = WatchRepairForm()

    context = {'form': form}

    return render(request, 'watch_repair/repairs.html', context)
