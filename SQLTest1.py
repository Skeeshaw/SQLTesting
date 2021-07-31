import discord
import mysql
import urllib

url = "http://192.168.1.148/password.html"
file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8")
    
TOKEN = decoded_line
##############################################
client = discord.Client()


@client.event
async def on_ready():
  print("Ready!")






client.run(TOKEN)