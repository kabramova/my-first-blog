from django.conf.urls import url
from . import views

# only an empty string will match this pattern
# it will tell Django that views.post_list is the right place to go if someone enters your website
# at the 'http://127.0.0.1:8000/' address.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
