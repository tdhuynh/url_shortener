
from django.conf.urls import url
from django.contrib import admin
from short_app.views import URLCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', URLCreateView.as_view(), name='url_create_view')
]
