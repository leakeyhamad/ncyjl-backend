from payments.models import Payment
from payments.tasks import process_payment

@action(detail=True, methods=["patch"])
def complete(self, request, pk=None):
    application = self.get_object()
    application.status = "completed"
    application.save()

    payment = Payment.objects.create(
        application=application,
        amount=5000
    )

    process_payment.delay(payment.id)

    return Response({"status": "completed and payment initiated"})
