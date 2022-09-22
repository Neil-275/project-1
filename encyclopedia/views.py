<<<<<<< HEAD
=======
from http.client import HTTPResponse
import re
>>>>>>> 7b09afe (KMP nz)
from django.shortcuts import render

from . import util
import time 
from wiki.views import to_main_page
from django.http import HttpResponse
from django import forms

class newTaskForm (forms.Form):
    entry= forms.CharField(label="Search Encyclopedia")

def index(request):
    entries= util.list_entries()
 
    return render(request, "encyclopedia/index.html", {
<<<<<<< HEAD
        "entries":entries,
    })
    
def to(request,name):
    check= util.get_entry(name)
    if (check==None):
        return render(request, "encyclopedia/error.html")
    else :  
        return render(request,"encyclopedia/info.html",{
            "val":check,"name":name.upper()
        })        
=======
        "entries": util.list_entries(),
        "form":newTaskForm()
    })

def to(request,name):
    info= util.get_entry(name);
    if (info==None):
        return render(request, "encyclopedia/error.html")
    else :  
        return render(request,"encyclopedia/test.html",{
            "val":info,"name":name.upper()
        })        
    
def search(request):
    matched_list=[]
    if (request.method == "POST"):
        form=newTaskForm(request.POST)
        if (form.is_valid()):
            name=form.cleaned_data["entry"]
            info=util.get_entry(name)
            if (not info==None):
                return render(request,"encyclopedia/info.html",{
                     "val":info,"name":name.upper()
                })
            list_name=util.list_entries()
            
            
            return render(request,"encyclopedia/index.html",{
                "entries":matched_list
            })

    return render(request, "encyclopedia/layout.html",{
        "form":newTaskForm()
    })
>>>>>>> 7b09afe (KMP nz)
