from django.shortcuts import render

def Invited(request):
    return render(request, 'invited/main.html')