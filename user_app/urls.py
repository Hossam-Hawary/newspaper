from django.conf.urls import url
from.import views


urlpatterns = [

    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),

]