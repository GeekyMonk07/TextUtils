# I am Anmol
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home") 

def analyze(request):
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinechar = request.POST.get('newlinechar', 'off')
    
    if removepunc == 'on':
        punctiations = '''!@#$%^&;:"'}{[]-+()'''
        analyzed = ""
        for char in text:
            if char not in punctiations:
                analyzed = analyzed + char
        params = {'purpose':'Removed', 'analyzed_text':analyzed}
        text = analyzed
        #return render(request, 'analyze.html', params)
        #return HttpResponse("Analyze")
    if (fullcaps == 'on'):
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'UPPERCASE', 'analyzed_text':analyzed}
        text = analyzed
        #return render(request, 'analyze.html', params)
    if (newlinechar == 'on'):
        analyzed = ''
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'NewLineRem', 'analyzed_text':analyzed}
        #return render(request, 'analyze.html', params)           
    
    if(removepunc != "on" and newlinechar != "on" and fullcaps != "on"):
        return HttpResponse("Sorry, You haven't selected any methods.")

    return render(request, 'analyze.html', params)
    
