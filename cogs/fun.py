import discord
import json
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'hellothere' in ''.join(message.content.lower().split()):
            with open('guilds.json', 'r') as f:
                guilds = json.load(f)

            if guilds[str(message.guild.id)][1] == 'text':
                await message.channel.send('General Kenobi')
            else:
                await message.channel.send('https://gfycat.com/freshgleamingfulmar')

    @commands.command()
    async def mode(self, ctx, medium=None):
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

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Fun(bot))
