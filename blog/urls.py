from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login_page, name='login_page'),
        url(r'^logout/$', views.logout_page, name='logout_page'),
        url(r'^new/$', views.create_post, name='create_post'),
        url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_view, name='post_view'),
]
