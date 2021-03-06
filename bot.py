import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os

client = commands.Bot(command_prefix="-")
client.remove_command('help')

@client.command()
async def dice(number1 = 1, number2 = 6):
    number = random.randint(number1, number2)
    await client.say(f"The dice rolled {number}.")

@client.command(pass_context = True)
async def stratos(ctx):
    await client.say(f"{ctx.message.author.mention} Geia, sas. What you're looking for can be found here, https://www.roblox.com/groups/4545549/Stratos-tou-Athinon \n \nThis is the main holder of all official infantries of Athenai, if you need any help finding the armies, they'll be found under the allies tab., if you need any assistance about an infantry and their speciality or how they operate, please contact the Genikos' of that certain infantry or any officers from it. \n \nhttps://docs.google.com/document/d/14jgeTUP6Qa2eI9Au76jwaHh-YJkqQyWeHI-TiWD8XbY/edit \n \n That document will provide you with more additional facts/requirements and descriptions about our infantries. \n \nThank you for having the patience to read this!")

@client.event()
async def on_message(ctx):
    if ctx.message == "@Stratos":
        await client.say(f"Hi there {ctx.message.author.mention}. My commands are `-dice` and `-stratos`.")

@client.event
async def on_ready():
    print("The bot is ready!")

bot_token:client.run(str(os.environ.get('BOT_TOKEN')))
