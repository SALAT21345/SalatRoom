from django.shortcuts import render

def game(request):
    return render(request, 'Game/Game.html')
