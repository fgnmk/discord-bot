import discord
from discord.ext import commands

bot = commands.bot(commands_prefix='[')

@bot.event
async def on_ready():
    print("bot is online")

bot.run("OTMwODI0MjQ5NjM4Mjc3MTMw.Yd7fog.XiIp1ZC5DWlkWEtiFr_DMNFCuE4")
