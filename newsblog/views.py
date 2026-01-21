from django.shortcuts import render

# Create your views here.


def news_list(request):
    # Logic to retrieve and display a list of news articles
    return render(request, 'newsblog/news_list.html')


def news_detail(request, id):
    # Logic to retrieve and display a specific news article by id
    return render(request, 'newsblog/news_detail.html', {'id': id})
