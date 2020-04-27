# i have created this website
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request,'index.html')

def analyze(request):

    djtext = request.POST.get('text','default value')
    removepuc= request.POST.get('removepunc','not checked')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    Extraspaceremover = request.POST.get('Extraspaceremover','off')

    if removepuc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext= analyzed
    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed}
        djtext= analyzed
    if newlineremover =="on":
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext= analyzed
    if Extraspaceremover =="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext= analyzed
    if newlineremover!= "on" and Extraspaceremover!= "on" and fullcaps!= "on" and removepuc!= "on":
        return HttpResponse("Error")
    return render(request,'analyze.html',params)


