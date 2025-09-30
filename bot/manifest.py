import os 
import json
from dotenv import load_dotenv

load_dotenv()

manifest = {
    "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.13/MicrosoftTeams.schema.json",
    "manifestVersion": "1.13",
    "version": "1.0.0",
    "id": os.getenv("APP_GUID"),
    "packageName": "com.example.hellobot",
    "developer": {
        "name": "Shah Noor",
        "websiteUrl": "https://example.com",
        "privacyUrl": "https://example.com/privacy",
        "termsOfUseUrl": "https://example.com/terms"
    },
    "name": { "short": "Hello Bot", "full": "Hello World Bot" },
    "description": { "short": "Test bot", "full": "A demo bot that replies in Teams" },
    "bots": [
        {
            "botId": os.getenv("MICROSOFT_APP_ID"),
            "scopes": ["personal", "team", "groupchat"],
            "supportsFiles": False,
            "isNotificationOnly": False
        }
    ],
    "permissions": ["identity", "messageTeamMembers"],
    "validDomains": [os.getenv("NGROK_DOMAIN")]
}

# Save manifest.json
with open("team_manifest/manifest.json", "w") as f:
    json.dump(manifest, f, indent=4)

print("manifest.json created successfully.")
