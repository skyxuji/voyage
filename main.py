import discord
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

block_words = [
    "Format Example: Blocked Word,"
]

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.author != client.user:
        content_lower = msg.content.lower().strip()
        author_roles = set(role.name for role in msg.author.roles)

        for text in block_words:
            if "Admin" not in author_roles and text in content_lower:
                await msg.delete()
                return

        print("Not Deleting...")

client.run("Bot Token")


