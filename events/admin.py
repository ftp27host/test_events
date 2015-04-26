from django.contrib import admin
from .models import Category, Event

class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'icon']

class EventAdmin(admin.ModelAdmin):
    firlds = ['title', 'logo', 'description', 'video', 'begin', 'end', 'category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)