import os
import uuid
from dotenv import load_dotenv

load_dotenv()


REQUIRED = ["HUBTEL_CLIENT_ID", "HUBTEL_CLIENT_SECRET", "HUBTEL_MERCHANT_ACCOUNT"]

for name in REQUIRED:
    print(name, bool(os.getenv(name)))

client_reference = uuid.uuid4().hex
print("clientReference:", client_reference)