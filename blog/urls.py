from django.conf.urls import url
from .views import post_all, post_detail, new_post, add_comment, post_delete, post_edit

urlpatterns = [
    url(r'^$', post_all, name='post_all'),
    url(r'^(?P<id>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^(?P<id>[0-9]+)/comment/$', add_comment, name='add_comment'),
    url('new_post', new_post, name='new_post'),
    url(r'^(?P<id>\d+)/post_delete/$', post_delete, name='post_delete'),
    url(r'^post_edit/(?P<id>\d+)/$', post_edit, name='post_edit'),
]