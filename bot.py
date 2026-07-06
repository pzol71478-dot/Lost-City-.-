import os
import discord
from discord.ext import commands
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# 1. سيرفر ويب وهمي عشان ريندر المجاني ما يعطي خطأ
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_web_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get('PORT', 8080))), MyServer)
    server.serve_forever()

# تشغيل سيرفر الويب في خلفية منفصلة
threading.Thread(target=run_web_server, daemon=True).start()

# 2. إعدادات البوت الأساسية
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_code="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت بنجاح باسم: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong! البوت شغال تمام")

# تشغيل البوت بالتوكن السري من ريندر
bot.run(os.getenv('DISCORD_TOKEN'))
