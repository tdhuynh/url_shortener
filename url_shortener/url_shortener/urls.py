
from django.conf.urls import url
from django.contrib import admin
from short_app.views import BookmarkCreateView, ShortView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BookmarkCreateView.as_view(), name='bookmark_create_view'),
    url(r'^(?P<short_url>\w+)/$', ShortView.as_view(), name='short_view'),

]
