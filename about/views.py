from django.shortcuts import render
from django.contrib.auth.models import User
from cheaterreports.models import CheaterPost, Comment
from newsblog.models import NewsPost

# Create your views here.


def about(request):
    """
    Fetch the about page. Numbers update on refresh.

    **Context**

    ``total_reports``
        The total number of cheater reports created.
    ``total_comments``
        The total number of comments across all reports.
    ``total_users``
        The total number of registered users.
    ``total_news``
        The total number of published news articles.
    """
    # Get total cheater reports
    total_reports = CheaterPost.objects.count()

    # Get total comments across all reports
    total_comments = Comment.objects.count()

    # Get total registered users
    total_users = User.objects.count()

    # Get total published news articles
    total_news = NewsPost.objects.filter(status=1).count()

    context = {
        'total_reports': total_reports,
        'total_comments': total_comments,
        'total_users': total_users,
        'total_news': total_news,
    }

    return render(request, 'about/about.html', context)
