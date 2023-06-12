import discord
import os

client = discord.Client()

block_words = [
    "retard",
    "nigga",
    "nigger",
    "migger",
    "miga",
    "neyger",
    "retarded",
    "mf",
    "n1gga",
    "n1ggers",
    "motherfucker",
    "gayass",
    "niqqa",
    "nig",
    "niqer",
    "mothertr",
    "mother fcker",
    "n!gga",
    "nyghas",
    
]



@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


@client.event
async def on_message(msg):

    if msg.author != client.user:

        for text in block_words:

            if "Moderator" not in str(msg.author.roles) and text in str(
                    msg.content.lower()):
                await msg.delete()
                return

        print("Not Deleting...")


client.run(os.getenv('TOKEN'))

