import discord
import asyncio
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "YOUR-TOKEN-HERE"
AUDIO_FILE = "YOUR-AUDIO-FILE-HERE"
CHANNEL_ID = YOUR-CHANNEL-ID-HERE
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        voice_channel = await channel.connect()
        while True:
            voice_channel.play(discord.FFmpegPCMAudio(AUDIO_FILE))
            while voice_channel.is_playing():
                await asyncio.sleep(1)
            await asyncio.sleep(15)
    else:
        print("Channel not found")

bot.run(TOKEN)