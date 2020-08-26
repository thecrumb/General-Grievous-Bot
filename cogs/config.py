import discord
import json
from discord.ext import commands

class Config(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def shutdown(self,ctx):
        print("shutdown")
        try:
            await self.client.logout()
        except:
            print("EnvironmentError")
            self.client.clear()

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('guilds.json', 'r') as f:
            guilds = json.load(f)

        guilds[str(guild.id)] = ['.', 'text']

        with open('guilds.json', 'w') as f:
            json.dump(guilds, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('guilds.json', 'r') as f:
            guilds = json.load(f)

        del guilds[str(guild.id)]

        with open('guilds.json', 'w') as f:
            json.dump(guilds, f, indent=4)

    @commands.command()
    async def changeprefix(self, ctx, prefix):
        with open('guilds.json', 'r') as f:
            guilds = json.load(f)

        guilds[str(ctx.guild.id)][0] = prefix

        with open('guilds.json', 'w') as f:
            json.dump(guilds, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')

def setup(client):
    client.add_cog(Config(client))
