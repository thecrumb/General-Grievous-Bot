import discord
import config
import json
from discord.ext import commands
from config import token

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = 'get_prefix')

client.state = 'text'

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'hellothere' in ''.join(message.content.lower().split()):
        if client.state == 'text':
            await message.channel.send('General Kenobi')
        else:
            await message.channel.send('https://gfycat.com/freshgleamingfulmar')
    await client.process_commands(message)

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) # FIXME use del or remove instead

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def mode(ctx, medium=None):
    if medium not in (None, 'text', 'gif'):
        await ctx.send('Please enter a valid mode.')
        return
    if medium != None:
        client.state = medium
    await ctx.send(f'Current mode: {client.state}')

client.run(token)
