from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.MobileHome_View.as_view(), name='home'),
    url(r'^signIn/', views.MobileSignIn_View.as_view(), name='signin'),
    url(r'^stations/', views.MobileStationView.as_view(), name='teststations'),
    url(r'^activetests/', views.MobileActive_View.as_view(), name='tests'),
    url(r'^settings/', views.MobileSettings_View.as_view(), name='settings'),
    url(r'^signOut/', views.MobileSignout_View.as_view(), name='signout'),
    url(r'^display_tests/', views.MobileDisplayTests_View.as_view(), name='display_tests'),
    )

