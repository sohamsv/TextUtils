from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Soham','place':'Mumbai'}
    return render(request, 'index.html', params)

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charactercount=="on":
        analyzed=""
        length = len(djtext)
        analyzed=analyzed+str(length)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charactercount!="on"):
        return HttpResponse("Please select any operation and try again...")

    return render(request, 'analyze.html', params)

def personalnavigator(request):
    navv=''' Navigation Bar <br> </h2>
    <a href= "https://sohamsv.github.io/"> Soham Vaidya's Portfolio </a><br>
    <a href="https://github.com/sohamsv"> Soham Vaidya's Github </a> <br>
    <a href="https://www.linkedin.com/in/soham-vaidya-05a4751b0/"> Soham Vaidya's Linkedln </a> <br>'''
    return HttpResponse(navv)