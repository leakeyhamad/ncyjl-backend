from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsYouth, IsOfficial
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsOfficial()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"], permission_classes=[IsYouth])
    def matched(self, request):
        profile = request.user.youthprofile
        jobs = Job.objects.filter(
            sub_county=profile.sub_county,
            is_open=True
        )
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)
