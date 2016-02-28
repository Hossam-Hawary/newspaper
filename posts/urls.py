from django.conf.urls import url
from.import views


urlpatterns = [
 

    url(r'home/',views.index_pag),
    url(r'^(?P<section_num>[0-9]+)/section$', views.index_pag1),
    url(r'^(?P<question_num>[0-9]+)/post$', views.postt),

]
