import discord
from discord.ext import commands
import random
import creds

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'Bot logged successfully as {client.user}!')

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

@client.command(aliases=["pallaotto", "8ball", "magicball"])
async def eightball(ctx, *, question):
    with open("src/response.txt", "r") as f:
        random_resp = f.readlines()
        response = random.choice(random_resp)
    await ctx.send(response)

@client.command()
async def mirror(ctx, *, text):
    user = ctx.author
    await ctx.send(f"{text} - sent by {user}")
        

client.run(creds.token)
