from django.contrib import admin
from django.urls import include, path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from channel import views as channel_view
from restframework.api import UserList, UserDetail, UserAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('channel/', include('channel.urls')),
    path('charts/', include('charts.urls')),
    path('djangoRT/', include('djangoRT.urls')),

    re_path(r'api/users_list/$', UserList.as_view(), name='user_list'),
    re_path(r'api/users_list/(?P<username>\d+)/$', UserDetail.as_view(), name='user_detail'),
    re_path(r'api/auth/$', UserAuthentication.as_view(), name='User Authentication API'),

    path('about', views.about, name="about"),
    path('', views.index, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)