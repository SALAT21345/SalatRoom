from django.shortcuts import render
import json
def Members(request):
    ListMembersInJson = 'allmembers/members.json'
    with open(ListMembersInJson, 'r', encoding='utf-8') as f:
        listMembers = json.load(f)
    return render(request, 'allmembers/allmembers.html', {'listMembers':listMembers})
