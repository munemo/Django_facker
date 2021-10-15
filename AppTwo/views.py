from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': 'Hello from AppTwo/index.html'}
    return render(request, 'AppTwo/index.html', context=my_dict)


def help(request):
    my_dict = {'insert_me': 'Welcome to the help page! How can i help you?'}
    return render(request, 'AppTwo/help.html', context=my_dict)

# Create your views here.
