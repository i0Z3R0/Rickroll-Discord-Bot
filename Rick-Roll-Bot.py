import string
import os
import discord
import asyncio
from discord.ext import commands

token = 'ODE2NjQzODI5OTU5NDkxNTg1.YD981Q.UC8JTUi4-O2X097Gyz-acq_gu1Y'

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print('Online')

createdChannels = []

@client.command(pass_context=True)
async def rickroll(ctx):
    print(f'Rickrolling {ctx.guild.name}')
    rickrollCat1 = await ctx.guild.create_category("Rick Roll")
    createdChannels.append(rickrollCat1)
    print("Category Made")
    rickRoll = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around", "and desert you", "Never gonna", "make you cry", "Never gonna say goodbye", "Never gonna tell a lie", "and hurt you"]
    for i in rickRoll:
        currentChannel = await ctx.guild.create_text_channel(i, category=rickrollCat1)
        await currentChannel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await currentChannel.send("https://cdn.discordapp.com/attachments/817018809701236746/817019597516963860/Rick_Roll_No_Watermark.gif")
        createdChannels.append(currentChannel)
        #await currentChannel.send(i.upper())
    print(f'Completed Rick Rolling Text Channels')
    rickrollCat2 = await ctx.guild.create_category("Rick Roll")
    createdChannels.append(rickrollCat2)
    for i in rickRoll:
        currentVC = await ctx.guild.create_voice_channel(i, category=rickrollCat2)
        createdChannels.append(currentVC)

@client.command(pass_context=True)
async def unroll(ctx):
    #print(createdChannels)
    for j in createdChannels:
        try:
            await j.delete()
        except:
            return
    print(f'Deleted {len(createdChannels)} Rickroll Channels in {ctx.guild.name} ')

@client.command(pass_context=True)
async def help(ctx):
    ctx.send("Commands: !rickroll Rick rolls the servers \n !unroll Deletes all rick roll channels")
    print("Help has been sent")

client.run(token, bot = True)
