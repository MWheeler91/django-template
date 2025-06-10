import requests # discord
from utils.common import catch_errors

# class DiscordBotSender(discord.Client):
#     def __init__(self, token, user_id, message):
#         super().__init__(intents=discord.Intents.default())
#         self.token = token
#         self.user_id = user_id
#         self.message = message

#     @catch_errors('discord')
#     async def on_ready(self):
#         try:
#             user = await self.fetch_user(self.user_id)
#             await user.send(self.message)
#             print(f"Message sent to {user}")
#         except Exception as e:
#             print(f"Failed to send message: {e}")
#         finally:
#             await self.close()

# @catch_errors('discord')
# def send_discord_dm(bot_token, user_id, message):
#     try:
#         url = "http://127.0.0.1:8000/send_dm/"
#         payload = {
#             "bot_token": bot_token,
#             "user_id": user_id,
#             "message": message
#         }

#         response = requests.post(url, json=payload, timeout=5)
#         response.raise_for_status()
#         return response.json()  # Should return {"status": "success", ...}
#     except requests.exceptions.RequestException as e:
#         client = DiscordBotSender(bot_token, user_id, message)
#         client.run(bot_token)
#         # return {"status": "error", "detail": str(e)}


    
