from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from cheaterreports.models import CheaterPost
from newsblog.models import NewsPost

# Create your views here.


def home(request):
    """
    Load the home page with recent cheater reports and latest news.

    **Context**

    ``recent_reports``
        The top 6 highest-scoring cheater reports from the last 30 days.
    ``latest_news``
        The 5 latest published news articles.

    **Template:**
    :template:`home/home.html`
    """
    # Get the 6 highest-scoring reports from the last 30 days
    one_month_ago = timezone.now() - timedelta(days=30)
    top_reports = CheaterPost.objects.filter(
        created_on__gte=one_month_ago
    ).order_by('-score')[:6]

    # Get the 5 latest published news articles
    latest_news = NewsPost.objects.filter(status=1).order_by('-created_on')[:5]

    context = {
        'recent_reports': top_reports,
        'latest_news': latest_news,
    }
    return render(request, 'home/home.html', context)
