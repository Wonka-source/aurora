from django.shortcuts import render
from .models import TeamMember


def all_staff(request):
    """A view that renders all team members on the about page"""

    team_members = TeamMember.objects.all()

    context = {'team_members': team_members}

    return render(request, 'staff/about.html', context)
