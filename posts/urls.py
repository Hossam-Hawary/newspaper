from django.conf.urls import url
from.import views


urlpatterns = [
 

    url(r'index/',views.index),
    url(r'^(?P<tag_id>[0-9]+)/tag$',views.tag),
    url(r'home/',views.home),
    url(r'^(?P<section_num>[0-9]+)/details$', views.details),
     url(r'home1',views.index_pag),
     url(r'^(?P<section_num>[0-9]+)/details1$', views.index_pag1),
     url(r'^(?P<question_num>[0-9]+)/post$', views.postt),

]
