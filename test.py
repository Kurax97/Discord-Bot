# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('token')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("NzE5Nzc2ODgzMzgxNjMzMDU0.Xt8Wsw.YprWfsPLiW0dqpt0SMTYRSV9rBw")
