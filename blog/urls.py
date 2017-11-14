from django.conf.urls import url
from . import views
from .views import home,listview,detailview,listviewAPI,PostCreate

app_name = 'blog'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^list/$', listview , name='listview'),
    url(r'^api/$',listviewAPI , name='api'),
    url(r'^list/(?P<pk>[0-9]+)/$' , detailview , name='detail'),

    url(r'Post/add/$', views.PostCreate.as_view(), name='add-post'),

    url(r'Post/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='update-post'),

    url(r'Post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='delete-post'),

    url(r'^search/$', views.searchview , name='searchview'),

    url(r'^signup/$', views.signup, name='signup'),
]