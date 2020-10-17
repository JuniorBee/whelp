from django.conf.urls import url
from django.urls import path

from .views import FileUploadView, FileStatusCheckView

urlpatterns = [
    url('create/', FileUploadView.as_view(), name='file-upload'),
    path('check/<uuid:pk>/', FileStatusCheckView.as_view(), name='file-check'),
]
