from django.http import HttpResponse
from django.shortcuts import render

def remove_punch(text):
    pun="""[][!"#$%&'()*+,./:;<=>?@\^_}`{|~-]"""
    temp_text=""
    for i in text:
        TOKEN=True
        for j in pun:
            if i==j:
                TOKEN=False
                break
                
        if (TOKEN):
             temp_text+=i
    
    return temp_text

def removeESpace(text):
    temp_text=""
    for i in range(len(text)-1):
        if text[i]==text[i+1]:
            pass
        else:
            temp_text+=text[i]

    return temp_text

def removeNEWLINE(text):
    temp_text=""
    for i in text:
        if i=="\n" or i=="\r":
            pass
        else:
            temp_text+=i

    return temp_text

def index(request):
    return render(request,"index.html")

def action(request):
    text = request.POST.get("text","default")
    uppercase= request.POST.get("uppercase","off")
    removepunch = request.POST.get("removepunch","off")
    removeExspace = request.POST.get("removeExspace","off")
    removeNewLine = request.POST.get("removeNewLine","off")


    if uppercase=="on":
         text=text.upper()
    
    if removepunch=="on":
        text=remove_punch(text)

    if removeExspace=="on":
        text=removeESpace(text)

    if removeNewLine=="on":
        text=removeNEWLINE(text)

    parameters={"response": text}

    return render(request,"action.html",parameters)
