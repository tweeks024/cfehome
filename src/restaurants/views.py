import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import RestaurantLocation

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    query_set = RestaurantLocation.objects.all()
    context = {
        "object_list": query_set
    }
    return render(request, template_name, context)
