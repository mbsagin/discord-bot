import os
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands

def get_champions(id):
    URL = "http://ddragon.leagueoflegends.com/cdn/9.24.2/data/en_US/champion.json"
    response = requests.get(URL)
    data = response.json()
    for champion in data['data']:
        if(data['data'][champion]['key'] == str(id)):
            print(data['data'][champion]['name'])

get_champions(266)