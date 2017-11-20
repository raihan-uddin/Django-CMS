from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.list_of_post, name='list_of_post'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
]