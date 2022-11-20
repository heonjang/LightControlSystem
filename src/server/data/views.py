from pstats import Stats
from re import S
from grpc import Status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from data.models import LightIntensityPoint
from data.serializer import LightIntensityPointSerializer


class LightIntensityPointViewSet(viewsets.ModelViewSet):
    queryset = LightIntensityPoint.objects.all().order_by("sensor")
    serializer_class = LightIntensityPointSerializer
    # permission_classes = [permission_classes.IsAuthenticated]

    @action(detail=True, methods=["get"])
    def points(self, request, pk: str):
        points = self.queryset.filter(sensor=pk).order_by("datetime")

        json = self.serializer_class(points, many=True)
        return Response(json.data)

    @action(detail=True, methods=["get"])
    def delete_all(self, requests, pk: str):
        self.queryset.filter(sensor=pk).delete()

        return Response(status.HTTP_200_OK)
