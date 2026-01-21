from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import NewsPost

# Create your views here.


def news_list(request):
    # Retrieve published news articles ordered by newest first
    posts = NewsPost.objects.filter(status=1).order_by('-created_on')

    # Pagination (6 posts per page)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
    }
    return render(request, 'newsblog/news_list.html', context)


def news_detail(request, id):
    # Retrieve a specific published news article by id
    post = get_object_or_404(NewsPost, pk=id, status=1)

    # Get recent articles (excluding current post)
    recent_posts = NewsPost.objects.filter(status=1).exclude(pk=id).order_by(
        '-created_on'
    )[:3]

    # Get previous article (older, so lower id or earlier date)
    previous_post = NewsPost.objects.filter(
        status=1, created_on__lt=post.created_on).order_by(
            '-created_on'
    ).first()

    # Get next article (newer, so higher id or later date)
    next_post = NewsPost.objects.filter(
        status=1, created_on__gt=post.created_on).order_by(
            'created_on'
    ).first()

    context = {
        'post': post,
        'recent_posts': recent_posts,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'newsblog/news_detail.html', context)
