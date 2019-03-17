from django.conf.urls import url
from mysite.views import home

urlpatterns = [
    url(r'', home, name="home"),
]
