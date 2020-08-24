import discord
import config
from config import token

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello there' in message.content.lower():
        await message.channel.send('General Kenobi')

client.run(token)
