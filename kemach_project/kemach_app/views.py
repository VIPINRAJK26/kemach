from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Machinery, TestDrive
from .serializers import MachinerySerializer, TestDriveSerializer

class MachineryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Machinery.objects.filter(available_for_test_drive=True)
    serializer_class = MachinerySerializer

class TestDriveViewSet(viewsets.ModelViewSet):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
  

class EnquiryViewSet(viewsets.ModelViewSet):
    pass