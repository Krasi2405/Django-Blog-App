from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.game_list, name = "game_list"),
	url(r'(?P<pk>\d+)/', views.game_detail, name = "game_detail"),
]