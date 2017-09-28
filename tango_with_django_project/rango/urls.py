from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^ejemplo/', views.ejemplo, name='ejemplo'),
    # url(r'^show_category/', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
]
