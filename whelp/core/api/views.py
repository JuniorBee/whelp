from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileCreateSerializer, FileRetrieveSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # TODO: Checking if extension is .pdf
        file_create_serializer = FileCreateSerializer(data=request.data)
        if file_create_serializer.is_valid():
            instance = file_create_serializer.save()
            file_retrieve_serializer = FileRetrieveSerializer(instance=instance)
            return Response(file_retrieve_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
