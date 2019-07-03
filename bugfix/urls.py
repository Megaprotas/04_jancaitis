from django.conf.urls import url
from .views import bugfix, new_bug, edit_bug, delete_bug, detail, vote, graph


urlpatterns = [
    url(r'^$', bugfix, name='bugfix'),
    url('bug_create', new_bug, name='new_bug'),
    url('graph', graph, name='graph'),
    url(r'^edit_bug/(?P<id>\d+)/$', edit_bug, name='edit_bug'),
    url(r'^(?P<id>\d+)/delete_bug/$', delete_bug, name='delete_bug'),
    url(r'^(?P<bug_id>[0-9]+)/$', detail, name='detail'),
    url(r'^(?P<bug_id>[0-9]+)/vote/$', vote, name='vote'),
]

