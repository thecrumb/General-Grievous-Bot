import discord
import setup
import json
import os
from discord.ext import commands
from setup import token

def get_prefix(bot, message):
    with open('guilds.json', 'r') as f:
        guilds = json.load(f)

    return guilds[str(message.guild.id)][0]

bot = commands.Bot(command_prefix = get_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Star Wars: Revenge of the Sith"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'cogs.{extension} loaded')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'cogs.{extension} unloaded')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'cogs.{extension} reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
