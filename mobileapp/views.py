from django.http import HttpResponse
from django.views.generic import View
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseBadRequest, Http404, JsonResponse
#from ..atg_general import models


class MobileSignIn_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('SignIn.html')
        #models.TestCases
        return HttpResponse(t.render())

class MobileStationView(View):
    def get(self, request, *args, **kwards):
        t = loader.get_template('Test_Station.html')
        station_id = request.GET.get('station')
        #stations = TestStation.objects.all()
        c = Context({
                'stations': 'hello'
            })
        print ('hello', station_id)

        return HttpResponse(t.render(c))

class MobileHome_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('Mobile_Home.html')
        return HttpResponse(t.render())

class MobileSignout_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('SignIn.html')
        return HttpResponse(t.render())

class MobileStations_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('Test_Station.html')
        return HttpResponse(t.render())

class MobileActive_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('ActiveTests.html')
        return HttpResponse(t.render())

class MobileSettings_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('MobileSettings.html')
        return HttpResponse(t.render())


