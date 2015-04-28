from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^categories/$', views.CategoryList, name='categoryList'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^now/$', views.categoriesNow, name='categoriesNow'),
]
