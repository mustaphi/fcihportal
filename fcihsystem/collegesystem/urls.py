from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login,name='login'),
    url(r'^complaint/', views.complaint,name='complaint'),
    url(r'^(?P<Registeration_id>[0-9]+)$', views.Register, name="Register"),
]