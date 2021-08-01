import discord
import urllib
import pymysql   
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='-')

url = "http://192.168.1.148/SQLpassword.html"
file = urllib.request.urlopen(url) #get connection to webpage and read string
for line in file:
    decoded_line = line.decode("utf-8")
    password = decoded_line

conn = pymysql.connect(
  host="localhost",
  user="heisenberg",
  password=password,
  database="test2"
)
  

##############################################
#discord bot section

url = "http://192.168.1.148/password.html"
file = urllib.request.urlopen(url) #get connection to webpage and read string

for line in file:
    decoded_line = line.decode("utf-8")
    
TOKEN = decoded_line

@bot.event
async def on_ready():
  print("Ready!") #prove the bot is on


@bot.command()
async def test(ctx, *, arg): #create command called test and pass through part of message after command
  channel = bot.get_channel(871141026105032774) #logs
  cur  = conn.cursor()
  query = f"" + arg + ""
  cur.execute(query)
  fetchall = cur.fetchall()
  await channel.send(fetchall)
  print("Action completed: " + fetchall)
  print(f"action completed")
  conn.commit()
  
    

bot.run(TOKEN)