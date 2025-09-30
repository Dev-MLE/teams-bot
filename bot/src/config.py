import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_ID = os.getenv("MicrosoftAppId")
    APP_PASSWORD = os.getenv("MicrosoftAppPassword")
    TENANT_ID = os.getenv("MicrosoftTenantId")
