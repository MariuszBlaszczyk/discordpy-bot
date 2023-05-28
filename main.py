# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")
    
@bot.command()
async def bbj(ctx):
    await ctx.send("Raków RKS !!!")
    
@bot.command()
async def ai(ctx, message):
    try:
        response = requests.post(os.environ["IP_MAKE"], data= {"message": message})
        if response.status_code == 200:
            await ctx.send("Sent message '(message)' to external IP. Response: {response.content)")
        else:
            await ctx.send("An error occurred while sending message (message)' to external IP. HTTP status code: (response.status_code}")
    except requests.exceptions.RequestException as e:
            await ctx.send(f" An error occurred while sending message '(message)' to external IP: {e}")

bot.run(os.environ["DISCORD_TOKEN"])
