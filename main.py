# This example requires the 'message_content' privileged intents

import os
import discord
import aiohttp
from discord.ext import commands


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
async def ai(ctx, text):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(os.environ["IP_MAKE"], data={'text': text}) as response:
                result = await response.text()
                await ctx.send(f"External IP response: {result}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
    

bot.run(os.environ["DISCORD_TOKEN"])
