import discord
import config
from discord.ext import commands
from config import token

client = commands.Bot(command_prefix = '.')

mode = 'text'

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'hello there' in message.content.lower():
        if mode == 'text':
            await message.channel.send('General Kenobi')
        else:
            await message.channel.send('https://gfycat.com/freshgleamingfulmar')

@client.command()
async def mode(ctx, medium=None):
    if medium not in (None, 'text', 'gif'):
        await ctx.send('Please enter a valid mode.')
        return
    if medium != None:
        mode = medium
    await ctx.send(f'Current mode: {mode}')

client.run(token)
