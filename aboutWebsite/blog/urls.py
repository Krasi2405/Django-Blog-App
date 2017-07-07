from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^$', views.blog_list, name = "list"),
	url(r'(?P<pk>\d+)/', views.blog_detail, name = "blog_detail"),
]