from django.http import HttpResponse
from django.views.generic import View
from django.template import loader

class MobileSignIn_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('SignIn.html')

        return HttpResponse(t.render())

class MobileHome_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('MobileHome.html')
        return HttpResponse(t.render())

class MobileSignout_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('SignIn.html')
        return HttpResponse(t.render())

class MobileStations_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('Test_Station.html')
        return HttpResponse(t.render())


