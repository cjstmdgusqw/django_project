from os import access
from django.shortcuts import render
from introduce.models import AcessLog

def introduce(request):
    # case 1 row
    access_log = AcessLog()
    access_log.location = "introduce"
    access_log.save()
     
    return render (request, 'cjs.html')



