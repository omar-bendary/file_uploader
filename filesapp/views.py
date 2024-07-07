import random

from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .models import UploadedFile
from .serializers import UploadedFileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    @action(detail=False, methods=["post"], parser_classes=[FileUploadParser])
    def upload(self, request):
        file_serializer = self.get_serializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def random_line(self, request, pk=None):
        file = self.get_object()
        lines = file.file.read().decode().splitlines()

        if not lines:
            return Response(
                {"error": "File is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        line = random.choice(lines)
        line_number = lines.index(line) + 1
        most_common_letter = max(set(line), key=line.count)

        response_data = {
            "line_number": line_number,
            "file_name": file.file.name,
            "line": line,
            "most_common_letter": most_common_letter,
        }

        accept = request.META.get("HTTP_ACCEPT", "text/plain")

        if accept == "application/json":
            return Response(response_data, status=status.HTTP_200_OK)
        elif accept == "application/xml":
            return Response(response_data, content_type="application/xml")
        else:
            return HttpResponse(line, content_type="text/plain")

    @action(detail=True, methods=["get"])
    def random_line_backwards(self, request, pk=None):
        file = self.get_object()
        lines = file.file.read().decode().splitlines()

        if not lines:
            return Response(
                {"error": "File is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        line = random.choice(lines)
        line_backwards = line[::-1]

        return HttpResponse(line_backwards, content_type="text/plain")

    @action(detail=False, methods=["get"])
    def longest_100_lines(self, request):
        all_lines = []
        for file in UploadedFile.objects.all():
            lines = file.file.read().decode().splitlines()
            all_lines.extend(lines)

        sorted_lines = sorted(all_lines, key=len, reverse=True)[:100]

        return Response(sorted_lines, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def longest_20_lines(self, request, pk=None):
        file = self.get_object()
        lines = file.file.read().decode().splitlines()

        sorted_lines = sorted(lines, key=len, reverse=True)[:20]

        return Response(sorted_lines, status=status.HTTP_200_OK)
