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
    await ctx.send("Choo choo! <@953629691691012167>  🚅")
    
@bot.command(brief='Podaj mi tekst do przetworzenia', usage='!ai <tekst>')
async def ai(ctx, *, text: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(os.environ["IP_MAKE"], data=text) as resp:
                if resp.status == 200:
                    response_text = await resp.text()
                    await ctx.send(response_text)
                else:
                    await ctx.send("Wystąpił problem, spróbuj ponownie później.")
        except:
            await ctx.send("Wystąpił problem, spróbuj ponownie później.")
        
bot.run(os.environ["DISCORD_TOKEN"])
