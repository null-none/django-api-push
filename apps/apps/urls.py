from django.conf.urls import url, patterns
from .views import PushView, AddIosDeviceView, AddAndroidDeviceView


urlpatterns = patterns('',
    url(r'^add/device/ios/', AddIosDeviceView.as_view(),  name='add_device_ios'),
    url(r'^add/device/android/', AddAndroidDeviceView.as_view(),  name='add_device_android'),
    url(r'^push/', PushView.as_view(),  name='push'),
)

