from django.conf.urls import url, patterns
from .views import AddIosDeviceView, AddAndroidDeviceView, PushAndroidView, PushIosView


urlpatterns = patterns('',
    url(r'^add/device/ios/', AddIosDeviceView.as_view(),  name='add_device_ios'),
    url(r'^add/device/android/', AddAndroidDeviceView.as_view(),  name='add_device_android'),
    url(r'^push/ios/', PushIosView.as_view(),  name='push_ios'),
    url(r'^push/android/', PushAndroidView.as_view(),  name='push_android'),
)

