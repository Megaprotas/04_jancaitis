from django.conf.urls import url
from .views import search_item

urlpatterns = [
    url(r'^$', search_item, name='search')
]