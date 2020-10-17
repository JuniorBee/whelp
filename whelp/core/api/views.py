from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from core.models import File, PDFContent
from core.tasks import ExtractPDFContent
from .serializers import FileCreateSerializer, FileRetrieveSerializer, FileStatusSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # TODO: Checking if extension is .pdf
        file_create_serializer = FileCreateSerializer(data=request.data)
        if file_create_serializer.is_valid():
            instance = file_create_serializer.save()
            file_retrieve_serializer = FileRetrieveSerializer(instance=instance)
            ExtractPDFContent().delay(instance.id)
            return Response(file_retrieve_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileStatusCheckView(APIView):
    def get(self, request, pk, *args, **kwargs):
        file = get_object_or_404(File, pk=pk)
        if PDFContent.objects.filter(file=file).exists():
            serializer = FileStatusSerializer({'file_id': file.pk, 'status': 'finished'})
        else:
            serializer = FileStatusSerializer({'file_id': file.pk, 'status': 'uploaded'})
        return Response(serializer.data)
