from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to render the index page """

    return render(request, 'home/index.html')


def about(request):
    """
    A view to return the process page
    """

    return render(request, 'home/about.html')


def consultation(request):
    """
    A view to return the process page
    """

    return render(request, 'home/consultation.html')


def contact(request):
    """
    A view to return the process page
    """

    return render(request, 'home/contact.html')


def process(request):
    """
    A view to return the process page
    """

    return render(request, 'home/process.html')
