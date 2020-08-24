import discord
import config
from discord.ext import commands
from config import token

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'hello there' in message.content.lower():
        await message.channel.send('https://gfycat.com/freshgleamingfulmar')

client.run(token)
