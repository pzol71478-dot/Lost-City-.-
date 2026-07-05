import discord
from discord.ext import commands
import os

# إعدادات البوت الأساسية
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تشغيل البوت بنجاح باسم: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong! البوت شغال تمام')


@bot.run('MTUyMDE2NzUyMjAwMjAxMDE0Mg.GdLekR.PlqlOSStV1w4pg1lUC3qN3E97gpMBlI9TBVsVc')

