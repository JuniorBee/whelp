from django.conf.urls import url
from .views import FileUploadView

urlpatterns = [
    url(r'^upload/$', FileUploadView.as_view(), name='file-upload'),
]
