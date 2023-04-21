from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    #analyzed=djtext


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}

    
    elif spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': "Removing Extra Space", 'analyzed_text': analyzed}


    elif newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': "Removing newline", 'analyzed_text': analyzed}

    elif capfirst == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Capitalizing Charcters", 'analyzed_text': analyzed}

    
    else:
        return HttpResponse("Error. Page not found!")
    return render(request,'analyze.html',params)

# def spaceremover(request):
#     return HttpResponse("space remover page")

# def capitalize():
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remover page")

# def charcount(request):
#     return HttpResponse("charcount page")