from django.shortcuts import render
from django.core import serializers
from .models import Category, Event
from django.views import generic
from django.http import HttpResponse
import datetime

def categoryList(request):
    data = serializers.serialize(
        'json', 
        Category.objects.all(), 
    )
    return HttpResponse(data)

def category(request, category_id):
    data = serializers.serialize(
        'json', 
        Event.objects.filter(category=category_id)
    )
    return HttpResponse(data)

def categoryNow(request):
    data = serializers.serialize(
        'json', 
        Event.objects.filter(begin__lte=datetime.date.today()).filter(end__gte=datetime.date.today())
    )
    return HttpResponse(data)  

def event(request, event_id):
    data = serializers.serialize(
        'json',
        Event.objects.filter(pk=event_id)
    )
    return HttpResponse(data)