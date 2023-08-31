#The client uses events to make it work
import os
import random
import discord 
import requests
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
  
@client.command(aliases = ["prompt"])
async def tell_story(ctx, *, prompt):
  try:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    text = response.choices[0].text
    await ctx.send(f'Prompt: {prompt} \n{text}')
    
  except Exception:
    message.channel.send("Error generating prompt")
    
@client.command(aliases = ["picture"])
async def generate_picture(ctx, *, prompt):
  def create_pictures(prompt):
  try:
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url
  except Exception:
    message.channel.send("Error generating image")

@client.command(aliases = ["amazon"])
    
  
client.run(os.getenv("JiaTOKEN"))
openai.api_key = os.getenv("JiaKey")
