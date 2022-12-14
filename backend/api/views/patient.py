from datetime import datetime
from rest_framework import viewsets, permissions

from api.models.patient import Patient
from api.serializers.patient import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted_at__isnull=True, profile=self.request.user).all()

    def perform_destroy(self, instance):
        return instance.save(deleted_at=datetime.now())
