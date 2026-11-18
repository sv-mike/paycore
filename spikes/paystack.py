import os
import httpx
from dotenv import load_dotenv

load_dotenv()

REQUIRED = ["PAYSTACK_SECRET_KEY", "SPIKE_CALLBACK_URL"]

initialize = httpx.post(
    "https://api.paystack.co/transaction/initialize",
    headers={"Authorization": "Bearer " + os.getenv("PAYSTACK_SECRET_KEY")},
    json={"email": "customer@email.com",
          "amount": "500000"}
    )

verify = httpx.get(
    "https://api.paystack.co/transaction/verify/rxgpws4992",
    headers = {"Authorization": "Bearer " + os.getenv("PAYSTACK_SECRET_KEY")},
    )

print(verify.json())


