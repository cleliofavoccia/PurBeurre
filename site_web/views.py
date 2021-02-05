from django.shortcuts import render


def index(request):
    """Print index.html in website"""
    context = None
    return render(request, 'index.html', context)


def legal_mentions(request):
    """Print legal_mentions.html in website"""
    return render(request, 'legal_mentions.html')