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
  
@client.event
async def on_message(message):
  if message.content.startswith('$hello'):
    if message.author.id == 207251811504095232:
      await message.channel.send("hi jun!")
    else:
      await message.channel.send("hello")
  if message.content.startswith('$num'):
    value = random.randint(0, 100)
    await message.channel.send("random value is " + str(value))
  await client.process_commands(message)
 
@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
  responses =  ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.event
async def on_join():
  
client.run(os.getenv("JiaTOKEN"))
