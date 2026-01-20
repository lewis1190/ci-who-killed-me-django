from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from cheaterreports.models import CheaterPost

# Create your views here.


def home(request):
    # Get the 6 highest-scoring reports from the last 30 days
    one_month_ago = timezone.now() - timedelta(days=30)
    top_reports = CheaterPost.objects.filter(
        created_on__gte=one_month_ago
    ).order_by('-score')[:6]

    context = {
        'recent_reports': top_reports,
    }
    return render(request, 'home/home.html', context)
