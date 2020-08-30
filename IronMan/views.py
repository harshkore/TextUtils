# I have created this file
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')
    # return HttpResponse('index')

def about(request):
    return HttpResponse("about <a href='/'>Back</a>")

def capital(request):
    return HttpResponse('capital')

def analyze(request):
    # Get the text
    djtext= request.POST.get('text','default')
    # Check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')



    if removepunc == "on":
        
        punctuations='''.!@#$%^&*()+-=_[];:""/|~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        djtext =  analyze
        params ={'purpose':'Removed Punctuations','analyzed_text':analyze}
        # return render(request,'analyze.html',params)
    
    if(fullcaps=="on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        djtext = analyze
        params ={'purpose':'Changed to UpperCase','analyzed_text':analyze}
        # return render(request,'analyze.html',params)
    
    if(newlineremover=="on"):
        analyze = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char
        djtext = analyze
        params ={'purpose':'Removed NewLines','analyzed_text':analyze}
        # return render(request,'analyze.html',params)

    if(extraspaceremover=="on"):
        analyze = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyze = analyze + char
        djtext = analyze
        params ={'purpose':'Extra Space Removed','analyzed_text':analyze}
        # return render(request,'analyze.html',params)

    if(charcounter=="on"):
        analyze = ""
        for char in djtext:
           if char != " ":
               analyze = analyze + char
        analyzed=('No. of characters given in the text are : '+str(len(analyze)))
        params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
      
    if(removepunc != "on" and fullcaps!="on" and charcounter!="on" and extraspaceremover!="on" and newlineremover!="on" ):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)