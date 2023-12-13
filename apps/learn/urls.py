from django.conf.urls import include
from django.urls import path, re_path
from apps.learn import views

urlpatterns = [

    # The home page
    path('learn', views.index, name='learn'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
