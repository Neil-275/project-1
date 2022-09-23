from ast import match_case
from random import choice
import re
from turtle import title
from django.shortcuts import render,redirect

from . import util,models
import time 
from wiki.views import to_main_page
from django.http import HttpResponse
from django import forms

class search_entry (forms.Form):
    entry= forms.CharField(label="Search Encyclopedia")

class new_page(forms.Form):
    title= forms.CharField(label="Title")
    info= forms.CharField(label="Infomation in Markdown content",widget=forms.Textarea)
    check=forms.IntegerField(widget=forms.HiddenInput(),initial=0) 

def index(request):
    entries= util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":search_entry()
    })

def to(request,name):
    info= util.get_entry(name);
    if (info==None):
        return render(request, "encyclopedia/error.html")
    else :  
        return render(request,"encyclopedia/info.html",{
            "val":info,"name":name.upper(),
            "form":search_entry()
        })        
    
def search(request):
    matched_list=[]
    if (request.method == "POST"):
        form=search_entry(request.POST)
        if (form.is_valid()):
            name=form.cleaned_data["entry"]
            info=util.get_entry(name)
            if (not info==None):
                return redirect("to",name=name)
            list_name=util.list_entries()
            for iname in list_name:
                if models.KMP(name,iname.lower())==True:
                    matched_list.append(iname)
            return render(request,"encyclopedia/index.html",{
                "entries":matched_list,
                "form":form
            })

    return render(request, "encyclopedia/layout.html",{
        "form":search_entry()
    })

def edit(request,name):
    info= util.get_entry(name)
    ok=1
    form= new_page(initial={'title':name,'info':info,'check':ok})
    # return HttpResponse(form.info)
    return render(request,"encyclopedia/newpage.html",{
        "form":form
     })
    

def create_new_page(request):
    if (request.method=="POST"):
        form=new_page(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            info=form.cleaned_data["info"]
            check=form.cleaned_data["check"]
            list_name=util.list_entries()
            if not check == 1 :
                for iname in list_name:
                    if iname.lower()==title.lower():
                        mess="You are posting an existing page. Find another article"
                        return render(request,"encyclopedia/newpage.html",{
                            "form": form,
                            "mess": mess
                        })
            util.save_entry(title.capitalize(),info)
            if check==1:
                return redirect("to",name=title)
            return redirect("index")
    return render(request,"encyclopedia/newpage.html",{
        "form":new_page()
    })
            
def rand(request):
    list_name=util.list_entries()
    entry=choice(list_name)    
    return redirect("to",name=entry)        
