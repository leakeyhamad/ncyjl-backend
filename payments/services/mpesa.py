import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

def get_access_token():
    response = requests.get(
        settings.MPESA_AUTH_URL,
        auth=HTTPBasicAuth(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
    )
    return response.json().get("access_token")


def send_b2c_payment(phone, amount, reference):
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "InitiatorName": settings.MPESA_INITIATOR_NAME,
        "SecurityCredential": settings.MPESA_SECURITY_CREDENTIAL,
        "CommandID": "BusinessPayment",
        "Amount": int(amount),
        "PartyA": settings.MPESA_SHORTCODE,
        "PartyB": phone,
        "Remarks": "NC-YJL Payment",
        "QueueTimeOutURL": settings.MPESA_TIMEOUT_URL,
        "ResultURL": settings.MPESA_RESULT_URL,
        "Occasion": reference
    }

    response = requests.post(
        settings.MPESA_B2C_URL,
        json=payload,
        headers=headers
    )

    return response.json()
