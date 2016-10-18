
from django.conf.urls import url, include
from django.contrib import admin
from short_app.views import BookmarkCreateView, ShortView, UserCreateView, BookmarkUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^$', BookmarkCreateView.as_view(), name='bookmark_create_view'),
    url(r'^(?P<pk>\d+)$', BookmarkUpdateView.as_view(), name='bookmark_update_view'),
    url(r'^(?P<short_url>\w+)/$', ShortView.as_view(), name='short_view'),

]
