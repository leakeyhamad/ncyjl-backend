from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.permissions import IsOfficial
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @action(detail=True, methods=["patch"], permission_classes=[IsOfficial])
    def hire(self, request, pk=None):
        application = self.get_object()
        application.status = "hired"
        application.save()
        return Response({"status": "hired"})
