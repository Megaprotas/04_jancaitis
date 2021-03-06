from django.conf.urls import url, include
from accounts.views import logout, login, registration, profile, edit_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^profile/edit_profile/$', edit_profile, name="edit_profile"),
    url(r'^password_reset/', include(url_reset)),
]