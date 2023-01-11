import os

import discord
from dotenv import load_dotenv

# This loads the bot's key
load_dotenv()

# Set up Discord bot and client
bot = discord.Client(intents=discord.Intents.all())

# add listeners here


# Run the bot using our token
bot.run(os.getenv("DISCORD"))
