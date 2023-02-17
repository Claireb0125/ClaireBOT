import os
import discord
import requests
import json
import random
from stay_online import stay_online

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)

ffxiv_words = [
  "ffxiv", "ff", "final fantasy", "mmo", "miss k", "chocobo", "ff14"
]

starter_ffxivquote = [
  "Have you heard of the critically acclaimed MMORPG Final Fantasy XIV? With an expanded free trial which you can play through the entirety of A Realm Reborn and the award winning Heavensward expansion up to level 60 for free with no restrictions on playtime."
]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  print(f"Received message: {message.content}")

  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in ffxiv_words):
    await message.channel.send(random.choice(starter_ffxivquote))

stay_online()
client.run(os.environ['TOKEN'])