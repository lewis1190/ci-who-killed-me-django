from django.shortcuts import render
from cheaterreports.models import CheaterPost

# Create your views here.


def home(request):
    # Get the 6 most recent reports
    recent_reports = CheaterPost.objects.all().order_by('-created_on')[:6]

    context = {
        'recent_reports': recent_reports,
    }
    return render(request, 'home/home.html', context)
