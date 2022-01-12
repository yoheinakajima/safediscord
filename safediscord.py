# bot.py
import os
import discord
from dotenv import load_dotenv
import requests
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id == #channel ID goes here##:
        print('channel')
        if message.author.id != #author ID goes here##:
            print('author')
            response = "Announcement above is from an unverified user, maybe we were hacked? Don't click on any links, I'm texting Yohei to look into this now."
            await message.channel.send(response)
            webhook_url = ##insert Zapier webhook here, and user Zapier to text yourself##
            data = { 'alert': 'yo'}
            requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})



client.run(TOKEN)


