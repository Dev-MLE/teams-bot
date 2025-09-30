# Teams Bot Production Guide

## Overview
This guide explains how to set up a Microsoft Teams bot that responds to messages. It covers Microsoft 365 navigation, Azure integration, authentication, bot configuration, Teams deployment, and optional Microsoft SDK usage. The goal is to provide a clear, production-ready workflow from credentials setup to Teams integration.

---

## 1. Prerequisites
- Microsoft 365 account with Teams access.
- Azure account for App registration and Bot resource.
- Python 3.13 and Poetry installed on your machine.
- Ngrok for exposing a local HTTPS endpoint to Teams.

---

## 2. Microsoft 365 and Azure Setup

### Microsoft 365 Tenant
- Sign in at the [Microsoft 365 Portal](https://portal.office.com) to access Teams.
- A Microsoft 365 tenant is required to test and deploy bots in Teams.
- Developer Program accounts provide sandbox environments for testing, but full production requires a real or paid tenant.
- Microsoft 365 Developer Program: [https://developer.microsoft.com/microsoft-365/dev-program](https://developer.microsoft.com/microsoft-365/dev-program)

### Azure App Registration
- Go to [Azure Portal](https://portal.azure.com), navigate to Azure Active Directory, and create a new App registration.
- Capture the following credentials:
  - Application ID (APP_GUID)
  - Client Secret (APP_PASSWORD)
  - Directory/Tenant ID (TENANT_ID)
- These credentials authenticate your bot with Microsoft 365 and Teams.
- Microsoft documentation on app registration: [https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

### Azure Bot Resource
- Create a Bot resource in Azure and link it to the App registration.
- Provides a Teams-compatible messaging endpoint.
- Enables your bot to receive and respond to Teams messages.
- For production, the bot endpoint must be HTTPS-accessible.
- Azure Bot Service documentation: [https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-overview](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-overview)

---

## 3. Authentication and Environment
- Store credentials securely in a `.env` file.
- The credentials needed include APP_GUID, APP_PASSWORD, TENANT_ID, and the HTTPS endpoint (e.g., Ngrok domain).
- These values allow your bot code to authenticate with Microsoft 365 and communicate with Teams.

---

## 4. Bot Implementation
- Your bot logic responds to messages from Teams instantly.
- The bot should handle any message and reply in real-time.
- App server exposes an endpoint (`/api/messages`) for Teams to send messages.
- The bot and app server together manage message processing, authentication, and response.

---

## 5. Local Development Workflow
- Run the bot locally using Python and your app server.
- Use Ngrok to expose your local server over HTTPS for Teams testing.
- Teams sends messages to the bot endpoint; the bot processes and responds instantly.
- This setup mimics production behavior without a public server.

---

## 6. Teams Integration
- Teams manifest defines:
  - Bot App ID
  - Messaging endpoint (HTTPS URL)
  - Valid domains for security
  - Scopes (personal, group chat, team)
- Upload manifest in Teams via "Apps → Upload a custom app".
- Once uploaded, any user in Teams can message the bot and receive real-time responses.

---

## 7. Microsoft Graph SDK (Optional)
- Microsoft Graph SDK allows the bot to fetch dynamic data from Microsoft 365 services.
- Provides programmatic access to Teams, SharePoint, OneDrive, etc.
- SDK documentation: [https://learn.microsoft.com/en-us/graph/sdks/sdks-overview](https://learn.microsoft.com/en-us/graph/sdks/sdks-overview)
- Useful for bots that respond with live data rather than static messages.

---

## 8. Production Considerations
- Microsoft 365 tenant and Azure Bot resource are compulsory for production deployment.
- Bot endpoint must be HTTPS-accessible and authenticated.
- Ngrok is only for local development; production requires a public host.
- Proper credential management ensures secure communication between Teams, Azure, and your bot.

---

## 9. Workflow Summary
1. Register App in Azure → obtain App ID, Secret, Tenant ID.
2. Create Bot resource → link to App registration.
3. Implement bot logic in Python → expose API endpoint via app server.
4. Use Ngrok locally for HTTPS testing.
5. Prepare Teams manifest with bot App ID and endpoint.
6. Upload manifest in Teams → bot is ready to receive and respond to messages.
7. Optionally, integrate Microsoft SDK for dynamic content from Microsoft 365.
