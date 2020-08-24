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

# @client.command()
# async def ping(ctx):
#     await ctx.send('Pong!')

# @client.command()
# async def mode(ctx, medium=None):
#     if medium not in (None, 'text', 'gif'):
#         await ctx.send('Please enter a valid mode.')
#         return
#     if medium != None:
#         client.state = medium
#     await ctx.send(f'Current mode: {client.state}')

client.run(token)
