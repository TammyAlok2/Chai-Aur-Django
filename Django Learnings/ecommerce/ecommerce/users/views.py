from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def hello (request):
    return JsonResponse({
        "status": "success",
        "data":{
            "name": "Hello, World!"
        },
        "message": "Hello, World!"
    })
