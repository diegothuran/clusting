from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clusters/$', views.ClusterizacaoList.as_view()),
]