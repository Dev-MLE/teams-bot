from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


'''class HelloBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        await turn_context.send_activity("Hello, I’m alive!")

    async def on_members_added_activity(
        self, members_added: list[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello, I’m alive!")'''

# src/bot.py
class HelloBot:
    async def on_message_activity(self, message_text: str):
        # Respond immediately for demo
        return {"text": f"Hello, I’m alive! You said: {message_text}"}

