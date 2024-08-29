from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Report
from .serializers import UserSerializer, ReportSerializer
from .permissions import IsAdministrator, CanAddReport, CanDeleteReport


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdministrator]


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_permission(self):
        if self.action in ['delete']:
            permission_classes = [CanDeleteReport]
        elif self.action in ['create']:
            permission_classes = [CanAddReport]
        else:
            permission_classes = [IsAdministrator]
        return [permission() for permission in permission_classes]