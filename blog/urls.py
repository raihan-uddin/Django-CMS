from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.list_of_post, name='list_of_post'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^backend/post/new/$', views.new_post, name='new_post'),
    url(r'^backend/post/$', views.list_of_post_backend, name='list_of_post_backend'),
    url(r'^backend/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^backend/(?P<slug>[-\w]+)/delete/$', views.delete_post, name='delete_post'),
]