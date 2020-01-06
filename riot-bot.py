import os
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='riot')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='summoner', help='Shows your summoner information.')
async def summoner(ctx, name):
    try:
        response = get_summoner(name)
        await ctx.send(response)
    except Exception as e:
        print(str(e))

@summoner.error
async def summoner_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('riot "SUMMONER NAME"')