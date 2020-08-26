import discord
import config
import json
from discord.ext import commands
from config import token

def get_prefix(client, message):
    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    return guilds[str(message.guild.id)][0]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'hellothere' in ''.join(message.content.lower().split()):
        with open('guilds.json', 'r') as f:
            guilds = json.load(f)

        if guilds[str(message.guild.id)][1] == 'text':
            await message.channel.send('General Kenobi')
        else:
            await message.channel.send('https://gfycat.com/freshgleamingfulmar')
    await client.process_commands(message)

@client.event
async def on_guild_join(guild):
    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    guilds[str(guild.id)] = ['.', 'text']

    with open('guilds.json', 'w') as f:
        json.dump(guilds, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    del guilds[str(guild.id)]

    with open('guilds.json', 'w') as f:
        json.dump(guilds, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    guilds[str(ctx.guild.id)][0] = prefix

    with open('guilds.json', 'w') as f:
        json.dump(guilds, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def mode(ctx, medium=None):
    if medium not in (None, 'text', 'gif'):
        await ctx.send('Please enter a valid mode.')
        return

    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    if medium != None:
        guilds[str(ctx.guild.id)][1] = medium

        with open('guilds.json', 'w') as f:
            json.dump(guilds, f, indent=4)

    await ctx.send(f'Current mode: {guilds[str(ctx.guild.id)][1]}')

client.run(token)
