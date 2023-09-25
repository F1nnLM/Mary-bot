import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot logged successfully as {client.user}!')

@client.command()
async def ping(ctx):
    await ctx.send("pong!")


client.run("MTE1NTc2NjkyMTE0MTE3MDE5Nw.GnUj_c.gdiLnWll8oLZpo4yTHF7UQJG19vsqV1DmslY0s")