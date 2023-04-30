#The client uses events to make it work
import os
import random
import discord 
from discord.ext import commands, tasks

#every bot command to start with a period
client = commands.Bot(command_prefix = ".") 

@client.event #this registers an event
async def on_ready():
  print('Jia bot is logged in as {0.user}'.format(client))
  #this is called when the bot is ready to start being used
