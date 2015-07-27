from django.http import HttpResponse
from push_notifications.models import APNSDevice, GCMDevice
from rest_framework.views import APIView


import json

from .models import *


class AddIosDeviceView(APIView):
    """
    Add iOS device.
    device -- Device parameter (format string)
    """

    def get(self, request, format=None):
        if request.GET.get('device', None):
            device = APNSDevice.objects.filter(registration_id=request.GET['device'])
            if not device:
                APNSDevice.objects.create(registration_id=request.GET['device'])
            result = {"result": "ok"}
        else:
            result = {"result": "error", 'type': 'invalid format device'}
        return HttpResponse(json.dumps(result), mimetype='application/json')


class AddAndroidDeviceView(APIView):
    """
    Add Android device.
    device -- Device parameter (format text)
    """

    def get(self, request, format=None):
        if request.GET.get('device', None):
            device = GCMDevice.objects.filter(registration_id=request.GET['device'])
            if not device:
                GCMDevice.objects.create(registration_id=str(request.GET['device']))
            result = {"result": "ok"}
        else:
            result = {"result": "error", 'type': 'invalid format device'}
        return HttpResponse(json.dumps(result), mimetype='application/json')


class PushView(APIView):
    """
    Push notification on device
    """
    def get(self, request, format=None):
        for item in APNSDevice.objects.all():
            try:
                item.send_message("Please update app")
            except Exception, e:
                pass
        for item in GCMDevice.objects.all():
            try:
                item.send_message("Please update app")
            except Exception, e:
                pass
        result = {"result": "ok"}
        return HttpResponse(json.dumps(result), mimetype='application/json')