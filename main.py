import discord
import asyncio
from discord.ext import commands

token = 'ODE2NjQzODI5OTU5NDkxNTg1.YD981Q.UC8JTUi4-O2X097Gyz-acq_gu1Y'

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is Online')

# Creates the list that will be used to store all the channels and VCs created
createdChannels = []

# Command to rick roll
@client.command(pass_context=True)
async def rickroll(ctx):
    print(f'Rickrolling {ctx.guild.name}')
    rickrollCat1 = await ctx.guild.create_category("Rick Roll")
    createdChannels.append(rickrollCat1)
    print("Category Made")
    rickRoll = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around", "and desert you", "Never gonna", "make you cry", "Never gonna say goodbye", "Never gonna tell a lie", "and hurt you"]
    # Iterates over every item in the list rickRoll and creates a channel with the name as the current iteration
    for i in rickRoll:
        currentChannel = await ctx.guild.create_text_channel(i, category=rickrollCat1)
        await currentChannel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await currentChannel.send("https://cdn.discordapp.com/attachments/817018809701236746/817019597516963860/Rick_Roll_No_Watermark.gif")
        createdChannels.append(currentChannel)
    print(f'Completed Rick Rolling Text Channels')
    rickrollCat2 = await ctx.guild.create_category("Rick Roll")
    createdChannels.append(rickrollCat2)
    # Does the same as before but with VCs
    for i in rickRoll:
        currentVC = await ctx.guild.create_voice_channel(i, category=rickrollCat2)
        createdChannels.append(currentVC)
    print(f'Completed Rick Rolling VCs')

# Deletes all created channels
@client.command(pass_context=True)
async def unroll(ctx):
    for j in createdChannels:
        try:
            await j.delete()
        except:
            return
    print(f'Deleted {len(createdChannels)} Rickroll Channels')

# Shows all the commands
@client.command(pass_context=True)
async def help(ctx):
    channel = ctx.channel
    embedVar = discord.Embed(title="Commands", description="", color=0x00ff00)
    embedVar.add_field(name="!rickroll", value="Rick rolls the server", inline=False)
    embedVar.add_field(name="!unroll", value="Deletes all rick roll channels", inline=False)
    embedVar.add_field(name="!help", value="Shows this message", inline=False)
    embedVar.add_field(name="!ping", value="Displays latency of bot in seconds", inline=False)
    await channel.send(embed=embedVar)
    print("Help has been sent")

# Shows latency of the bot
@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.channel
    await channel.send(f'Pong! {client.latency}!')

client.run(token, bot = True)
