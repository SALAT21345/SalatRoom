from django.shortcuts import render
import json
def index(request):
    return render(request, 'SalatSite/Index.html')
