from django.conf.urls import url
from.import views
from user_app.views import *


urlpatterns = [

    url(r'^register/$', views.register),

    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    
    

]
