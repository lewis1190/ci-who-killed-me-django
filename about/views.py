from django.shortcuts import render
from django.contrib.auth.models import User
from cheaterreports.models import CheaterPost, Comment
from newsblog.models import NewsPost

# Create your views here.


def about(request):
    # Get total cheater reports
    total_reports = CheaterPost.objects.count()

    # Get total comments across all reports
    total_comments = Comment.objects.count()

    # Get total registered users
    total_users = User.objects.count()

    # Get total news articles
    total_news = NewsPost.objects.count()

    context = {
        'total_reports': total_reports,
        'total_comments': total_comments,
        'total_users': total_users,
        'total_news': total_news,
    }

    return render(request, 'about/about.html', context)
