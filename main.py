import discord
from discord.ext import commands
from random import randint
import random
import asyncio
from random import choice

DISCORD_TOKEN = 'YOUR TOKEN'

##Let's do a watching status for example
activity = discord.Activity(type=discord.ActivityType.watching, name="shrek 2")

bot = commands.Bot(command_prefix="YOUR PREFIX", activity=activity)

##You have to add a mp3 file path in "MP3" list, for example "C:/Users/User/music.mp3"
MP3 = ["C:/Users/User/Desktop/"]


@bot.command(aliases=['mp3','paly'])
async def play(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None

    if voice_channel != None:
        source = str(random.choice(MP3)) ##You can use choice module to play random MP3.
        # source = str("C:/Users/User/Desktop/") ##Or you can play specific music
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg-4.4-essentials_build/ffmpeg-4.4-essentials_build/bin/ffmpeg.exe", source=source))
        # Sleep while audio is playing.
        while vc.is_playing():
            await asyncio.sleep(1)

        else:
            await asyncio.sleep(1)

            while vc.is_playing():
                break
            else:
                await vc.disconnect()

        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "You are not in a channel.")

    # await ctx.message.delete()