from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Job
from applications.models import Application
from payments.models import Payment

class SummaryView(APIView):
    def get(self, request):
        return Response({
            "total_jobs": Job.objects.count(),
            "total_applications": Application.objects.count(),
            "total_paid": sum(
                p.amount for p in Payment.objects.filter(status="paid")
            )
        })
