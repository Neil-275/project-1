from django.shortcuts import render

from . import util
import time 
from wiki.views import to_main_page
from django.http import HttpResponse

def index(request):
    entries= util.list_entries()
 
    return render(request, "encyclopedia/index.html", {
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