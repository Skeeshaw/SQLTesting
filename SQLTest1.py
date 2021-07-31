import discord
import urllib
import mysql.connector
import pymysql    
client = discord.Client()
  
conn = pymysql.connect(
  host="localhost",
  user="root",
  password="5182",
  database="test2"
)
  
# Create a cursor object
cur  = conn.cursor()
  
first_name = '1201'
last_name = 'PRI'
  
#query = f"INSERT INTO test1 (first_name, last_name) VALUES ('{first_name}', '{last_name}')"
  
cur.execute(query)
print(f"{cur.rowcount} details inserted")
conn.commit()
conn.close()


##############################################
#i believe pymysql can also read lines but i do not want to test it right now so i will keep using mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5182",
  database="test2"
)

mycursor = mydb.cursor()

test = 'FROM'
#mycursor.execute("SELECT * " + test + " test1")

myresult = mycursor.fetchall()

print(myresult)

##############################################
#discord bot section

url = "http://192.168.1.148/password.html"
file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8")
    
TOKEN = decoded_line

'''
#set all user-made and automatic variables. testing this, may switch this in the future
first_variable = 
second_variable = 
third_variable = 
fourth_variable = 
fifth_variable = 
sixth_variable = 
'''
@client.event
async def on_ready():
  print("Ready!")