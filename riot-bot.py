import os
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
RIOT_TOKEN = os.getenv('RIOT_TOKEN')

bot = commands.Bot(command_prefix='..')

def get_summoner(name, region):
    URL = "https://"+region+"1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name
    head = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": RIOT_TOKEN,
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78"
    }
    response = requests.get(url = URL, headers = head)
    data = response.json()
    return data
    

def get_league(linkID, region):
    URL = "https://"+region+"1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + linkID
    head = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": RIOT_TOKEN,
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78"
    }
    response = requests.get(url = URL, headers = head)
    data = response.json()
    return data


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='summoner', help='Shows your summoner information.')
async def summ(ctx, name, region):
    try:
        response = get_summoner(name, region)
        league = get_league(response['id'], region)
        imgURL = 'http://ddragon.leagueoflegends.com/cdn/9.24.2/img/profileicon/' + str(response['profileIconId'])+ '.png'

        embedFile = discord.Embed(
            title = "League of Legends",
            colour = discord.Colour.blue())
        embedFile.set_thumbnail(url=imgURL)
        embedFile.add_field(name = "Summoner Name", value = response['name'], inline = True)
        embedFile.add_field(name = "Summoner Level", value = str(response['summonerLevel']), inline = True)
        embedFile.add_field(name = "\u200b", value = "\u200b", inline = False)
        for item in league:
            embedFile.add_field(name = item['queueType'], value = item['tier']+'-'+item['rank'], inline = True)
            embedFile.add_field(name = "League Point", value = str(item['leaguePoints']), inline = True)
            embedFile.add_field(name = "Win/Lose", value = str(item['wins'])+'/'+str(item['losses']), inline = True)
        await ctx.send(embed = embedFile)
    except Exception as e:
        print(str(e))


@summ.error
async def summ_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command => ..summoner "SUMMONER NAME" "REGION", euw,na,tr...')


bot.run(TOKEN)