from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupckate!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, '../templates/rango/index.html', context=context_dict)

    # return HttpResponse('<h1>Hello World!</h1><br><h2><a href=/rango/about>Jump to about</a>')

def about(request):
    return HttpResponse('Rango says here is the about page')

def ejemplo(request):
    context_dict = {'boldmsg' : "You know what is it", 'gjmsg' : "Goood Job!"}

    return render(request, '../templates/rango/ejemplo.html', context=context_dict)
