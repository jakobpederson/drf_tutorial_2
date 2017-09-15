# Finally we need to wire these views up. Create the snippets/urls.py file:
from django.conf.urls import url
from snippets import views


urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
