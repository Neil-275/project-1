from django.shortcuts import redirect
from django.http import HttpResponse

def to_main_page(request):
    return redirect("/wiki/")
    # return HttpResponse("Hello?")