import uvicorn
from fastapi import FastAPI, Request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from src.config import Config
from src.bot import HelloBot
'''
# Adapter with credentials
settings = BotFrameworkAdapterSettings(Config.APP_ID, Config.APP_PASSWORD)
adapter = BotFrameworkAdapter(settings)
bot = HelloBot()

app = FastAPI()

@app.post("/api/messages")
async def messages(req: Request) -> Response:
    body = await req.json()
    activity = Activity().deserialize(body)

    auth_header = req.headers.get("Authorization", "")

    async def call_bot(turn_context: TurnContext):
        await bot.on_turn(turn_context)

    response = await adapter.process_activity(activity, auth_header, call_bot)
    if response:
        return Response(content=response.body, status_code=response.status)
    return Response(status_code=201)

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=3978, reload=True)
'''

# src/app.py
import os
from fastapi import FastAPI, Request
from src.bot import HelloBot

app = FastAPI()
bot = HelloBot()

@app.post("/api/messages")
async def messages(req: Request):
    data = await req.json()
    text = data.get("text", "")
    response = await bot.on_message_activity(text)
    return response
