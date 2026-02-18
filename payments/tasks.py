from celery import shared_task
from .models import Payment
from .services.mpesa import send_b2c_payment

@shared_task
def process_payment(payment_id):
    payment = Payment.objects.get(id=payment_id)

    response = send_b2c_payment(
        phone=payment.application.youth.youthprofile.phone_number,
        amount=payment.amount,
        reference=str(payment.application.id)
    )

    if "ConversationID" in response:
        payment.status = "processing"
        payment.transaction_id = response["ConversationID"]
    else:
        payment.status = "failed"

    payment.save()
