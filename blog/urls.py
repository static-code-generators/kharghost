from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_view, name='post_view'),
]