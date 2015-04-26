from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^categories/$', views.categoryList, name='categoryList'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
]
