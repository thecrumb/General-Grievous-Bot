import discord
import setup
import json
import os
from discord.ext import commands
from setup import token

def get_prefix(client, message):
    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    return guilds[str(message.guild.id)][0]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'cogs.{extension} loaded')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'cogs.{extension} unloaded')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send(f'cogs.{extension} reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
