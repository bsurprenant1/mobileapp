from django.views.generic import View
from django.template import loader, Context
from django.http import HttpResponse, JsonResponse
import json
#import urllib2
import requests

class MobileSignIn_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('SignIn.html')
        return HttpResponse(t.render())

class MobileStationView(View):
    def get(self, request, *args, **kwards):
        t = loader.get_template('Test_Station.html')
        json_file = open('station_info.json')
        data = json_file.read()
        json_file.close()
        json_data = json.loads(data)

        c = Context({
            'stations': json_data["stations"]
        })

        #print json_data["stations"]
        return HttpResponse(t.render(c))


class MobileDisplayTests_View(View):
    """
    Displays available tests for a given station
    """
    def get(self, request):
    #    station_id = request.GET.get("station_id")
        t = loader.get_template('list_station_tests.html')

        #req = requests.get("http://localhost:8080/tests")
        #req_data = req.json()

        #test_categories = req_data.keys()
        #print test_categories
        #print data["tests_aux"]
        #c = Context({
        #    'tests': req_data
        #})
        #print data

        #return JsonResponse(json_data["available_tests"], safe=False)
        #return HttpResponse("You selected station: " + str(station_id))


        return HttpResponse(t.render())



class MobileHome_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('Mobile_Home.html')
        return HttpResponse(t.render())

class MobileSignout_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('SignIn.html')
        return HttpResponse(t.render())

class MobileActive_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('ActiveTests.html')
        return HttpResponse(t.render())

class MobileSettings_View(View):
    def get(self, request, *args, **kwargs):
        t = loader.get_template('MobileSettings.html')
        return HttpResponse(t.render())


