from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('events.urls', namespace='events')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
