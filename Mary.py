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
    with open("response.txt", "r") as f:
        random_resp = f.readlines()
        response = random.choice(random_resp)
    await ctx.send(response)

@client.command()
async def mirror(ctx, *, text):
    user = ctx.author
    await ctx.send(f"{text} - sent by {user}")

@client.command()
async def math(ctx, a: int, op, b: int):
    if (op == "+"):
        answer = a + b
    elif (op == "-"):
        answer = a - b
    elif (op == "*"):
        answer = a * b
    elif (op == "/"):
        answer = a / b
    else:
        answer = "ERROR: Unknown operation type use +, -, * or / to specify it"

    await ctx.send(answer)

client.run(creds.token)
