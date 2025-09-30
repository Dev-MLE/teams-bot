# Teams Bot Requirements 

## 1. Microsoft 365 Tenant

**Purpose:**  
- The tenant provides a Teams environment where your bot can operate.  
- All Teams messages and channels are hosted in a tenant.  
- Required for testing and production deployment.

**Setup Instructions:**  
1. Sign in to Microsoft 365: [https://portal.office.com](https://portal.office.com)  
2. If you don’t have a tenant:
   - Join the [Microsoft 365 Developer Program](https://developer.microsoft.com/en-us/microsoft-365/dev-program) to get a sandbox tenant (for testing).  
   - For production, a paid or organization-provided tenant is required.  

**Reference:**  
- [Microsoft 365 Documentation](https://learn.microsoft.com/en-us/microsoft-365/)

---

## 2. Azure App Registration

**Purpose:**  
- Provides authentication credentials so your bot can securely communicate with Microsoft 365 and Teams.  
- Generates:
  - **Application (Client) ID** → `APP_GUID`  
  - **Client Secret** → `APP_PASSWORD`  
  - **Tenant ID** → `TENANT_ID`  

**Setup Instructions:**  
1. Go to [Azure Portal](https://portal.azure.com/) → Azure Active Directory → **App registrations** → **New registration**.  
2. Name your application.  
3. Select supported account types (usually “Accounts in this organizational directory only”).  
4. Note the **Application (client) ID** and **Directory (tenant) ID**.  
5. Generate a **Client Secret** under **Certificates & secrets**.  

**Reference:**  
- [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

---

## 3. Azure Bot Resource

**Purpose:**  
- Connects your Azure App Registration to Teams.  
- Provides a messaging endpoint for your bot.  
- Enables Teams channels integration and secure message delivery.

**Setup Instructions:**  
1. In [Azure Portal](https://portal.azure.com/) → **Create a resource** → Search for **Bot Channels Registration** → **Create**.  
2. Link the bot to your previously registered Azure App.  
3. Configure messaging endpoint (for local development, use Ngrok HTTPS URL; for production, use a hosted HTTPS endpoint).  
4. Enable Teams channel integration in **Channels** tab.  

**Reference:**  
- [Azure Bot Service Overview](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-overview)  
- [Configure a bot for Microsoft Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/create-a-bot-for-teams)

---

**Summary:**  
- **Microsoft 365 Tenant** → Hosts Teams environment  
- **Azure App Registration** → Provides authentication credentials  
- **Azure Bot Resource** → Connects app to Teams and hosts endpoint  

All three are mandatory for running a Teams bot in any real environment. Local development can temporarily use Ngrok, but production requires these resources.
