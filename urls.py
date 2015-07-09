from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.MobileHome_View.as_view(), name='mobile'),
    url(r'^signIn/', views.MobileSignIn_View.as_view(), name='signin'),
    url(r'^signOut/', views.MobileSignout_View.as_view(), name='signout'),
    )

