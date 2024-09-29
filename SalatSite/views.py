from django.shortcuts import render
import json
def index(request):
    ListMembersInJson = 'SalatSite/members.json'
    with open(ListMembersInJson, 'r', encoding='utf-8') as f:
            listMembers = json.load(f)
    return render(request, 'SalatSite/Index.html', {'listMembers':listMembers})

# def news(request):
#     return render(request, 'SalatSite/news.html')
