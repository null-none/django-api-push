from django.http import HttpResponse
from push_notifications.models import APNSDevice, GCMDevice
from rest_framework.views import APIView

import json

from .models import *
from .serializers import *

class AddIosDeviceView(APIView):
    """
    Add iOS device.
    device -- Device parameter (format string)
    """

    def post(self, request, format=None):
        if request.POST.get('device', None):
            device = APNSDevice.objects.filter(registration_id=request.POST['device'])
            if not device:
                APNSDevice.objects.create(registration_id=request.POST['device'])
            result = {"result": "ok"}
        else:
            result = {"result": "error", 'type': 'invalid format device'}
        return HttpResponse(json.dumps(result), mimetype='application/json')


class AddAndroidDeviceView(APIView):
    """
    Add Android device.
    device -- Device parameter (format text)
    """

    def post(self, request, format=None):
        if request.POST.get('device', None):
            device = GCMDevice.objects.filter(registration_id=request.POST['device'])
            if not device:
                GCMDevice.objects.create(registration_id=str(request.POST['device']))
            result = {"result": "ok"}
        else:
            result = {"result": "error", 'type': 'invalid format device'}
        return HttpResponse(json.dumps(result), mimetype='application/json')


class PushAndroidView(APIView):
    """
    Push notification on device android
    """
    def get(self, request, format=None):
        for item in GCMDevice.objects.all():
            try:
                item.send_message("Please update app")
            except Exception, e:
                result = {"result": str(e)}
                return HttpResponse(json.dumps(result), mimetype='application/json')
        result = {"result": "ok"}
        return HttpResponse(json.dumps(result), mimetype='application/json')


class PushIosView(APIView):
    """
    Push notification on device iOS
    """
    def get(self, request, format=None):
        for item in APNSDevice.objects.all():
            try:
                item.send_message("Please update app")
            except Exception, e:
                result = {"result": str(e)}
                return HttpResponse(json.dumps(result), mimetype='application/json')
        result = {"result": "ok"}
        return HttpResponse(json.dumps(result), mimetype='application/json')
