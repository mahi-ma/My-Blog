from django.conf.urls import url
from .views import home,listview,detailview,listviewAPI

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^list/$', listview , name='listview'),
    url(r'^api/$',listviewAPI , name='api'),
    url(r'^blog/(?P<pk>(\d+)+)/$' , detailview , name='detail')

]