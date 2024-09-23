from django.shortcuts import render

def index(request):
    return render(request, 'SalatSite/index.html')

# def news(request):
#     return render(request, 'SalatSite/news.html')
