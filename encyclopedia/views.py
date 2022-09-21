from http.client import HTTPResponse
from django.shortcuts import render

from wiki.views import to_main_page

from . import util
import time 
from wiki.views import to_main_page
from django.http import HttpResponse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def to(request,name):
    check= util.get_entry(name);
    if (check==None):
        return render(request, "encyclopedia/error.html")
        # HttpResponse("Hello???")
        # time.sleep(2)
        # return to_main_page
    else :  
        return render(request,f"entries/{name}.md")
        


