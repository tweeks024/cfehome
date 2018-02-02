import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):
    num = random.randint(0, 100000)
    return render(request, "base.html", {"html_var": "some context variable", "num": num})
