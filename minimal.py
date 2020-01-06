import os
import requests
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
USERNAME = os.getenv('IMGFLIP_USERNAME')
PASS = os.getenv('IMGFLIP_PASSWORD')

bot = commands.Bot(command_prefix='..')

def get_crypto(coin):
    URL = 'https://api.coinmarketcap.com/v1/ticker/'+coin
    response = requests.get(URL)
    data = response.json()
    return float(data[0]['price_usd'])


def get_memes():
    URL = 'https://api.imgflip.com/get_memes'
    r = requests.get(URL)

    data = r.json()
    for meme in data['data']['memes']:
        print(meme['id'] + ' | ' + meme['name'] + ' | ' + meme['url'])


def create_meme(t1, t2, t_id):
    URL = 'https://api.imgflip.com/caption_image'
    data = {'template_id': t_id,
            'username': USERNAME,
            'password': PASS,
            'text0': t1,
            'text1': t2,
            }
    r = requests.post(url=URL, data=data)
    data = r.json()
    return data['data']['url']

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='coin', help='Shows price of crypto coin')
async def coin(ctx, coin):
    try:
        response = get_crypto(coin)
        await ctx.send(response)
    except Exception as e:
        print(str(e))


@coin.error
async def coin_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('..coin "Name of coin"')


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='batman', help='Batman slapping Robin')
async def batman_meme(ctx, t1, t2):
    yazi1 = ''
    yazi2 = ''
    try:
        if t1 is not None:
            yazi1 = t1
        if t2 is not None:
            yazi2 = t2
        response = create_meme(yazi1, yazi2, 438680)
        await ctx.send(response)
    except Exception as e:
        print(str(e))


@batman_meme.error
async def batman_meme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('..batman "text1" "text2"')


@bot.command(name='isthis', help='Is this a butterfly')
async def isthis_meme(ctx, t1, t2):
    yazi1 = ''
    yazi2 = ''
    try:
        if t1 is not None:
            yazi1 = t1
        if t2 is not None:
            yazi2 = t2
        response = create_meme(yazi1, yazi2, 100777631)
        await ctx.send(response)
    except Exception as e:
        print(str(e))


@isthis_meme.error
async def isthis_meme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('..isthis "text1" "text2"')


@bot.command(name='matrix', help='Matrix Morpheus')
async def matrix_meme(ctx, t1, t2):
    yazi1 = ''
    yazi2 = ''
    try:
        if t1 is not None:
            yazi1 = t1
        if t2 is not None:
            yazi2 = t2
        response = create_meme(yazi1, yazi2, 100947)
        await ctx.send(response)
    except Exception as e:
        print(str(e))


@matrix_meme.error
async def matrix_meme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('..matrix "text1" "text2"')


@bot.command(name='mind', help='Change my mind')
async def mind_meme(ctx, t1, t2):
    yazi1 = ''
    yazi2 = ''
    try:
        if t1 is not None:
            yazi1 = t1
        if t2 is not None:
            yazi2 = t2
        response = create_meme(yazi1, yazi2, 129242436)
        await ctx.send(response)
    except Exception as e:
        print(str(e))


@mind_meme.error
async def mind_meme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('..mind "text1" "text2"')


@bot.command(name='imagine', help='Sponge Bob imagination, rainbow')
async def imagine_meme(ctx, t1, t2):
    yazi1 = ''
    yazi2 = ''
    try:
        if t1 is not None:
            yazi1 = t1
        if t2 is not None:
            yazi2 = t2
        response = create_meme(yazi1, yazi2, 163573)
        await ctx.send(response)
    except Exception as e:
        print(str(e))


@imagine_meme.error
async def imagine_meme_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('..imagine "text1" "text2"')
        

bot.run(TOKEN)