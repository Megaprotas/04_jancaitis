from django.conf.urls import url, include
from .views import all_features, newest_feature, feature_detail


urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^newest_feature/$', newest_feature, name='newest_feature'),
    url(r'^(?P<feature_id>[0-9]+)/$', feature_detail, name='feature_detail'),
]

