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
    context = {
        'post': post,
    }
    return render(request, 'newsblog/news_detail.html', context)
