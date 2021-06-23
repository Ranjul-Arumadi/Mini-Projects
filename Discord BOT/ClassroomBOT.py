#ClassRoom Bot for Discord
import os
import discord
from datetime import datetime
import pytz
import requests
import json
from keep_alive import keep_alive
from replit import db

db["OS"] = "https://meet.google.com/swk-hxqh-gja"
db["GT"] = "https://meet.google.com/wpi-sbpx-bbo"
db["COA"] = "https://meet.google.com/wah-cuzd-zgp"
db["Ethics"] = "http://meet.google.com/tov-dgys-gky"
db["Constitution"] = "https://meet.google.com/rna-fdxd-wzi"
db["DBMS"] = "https://meet.google.com/ieu-mysc-bnx"
db["Digital_Lab"] = "https://meet.google.com/qhb-tten-itu"
db["OS_Lab"] = "https://meet.google.com/ywm-ehfy-nvj"
db["Minor"] = "https://meet.google.com/squ-idzq-ury"
db["Honors"] = "https://meet.google.com/saj-htnf-nnw"

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)



client = discord.Client()


@client.event
async def on_ready():
  print(f'We have logged in as {client}')

tz_IN = pytz.timezone('Asia/Kolkata') 
datetime_IN = datetime.now(tz_IN)
print(f'Hour : {datetime_IN.hour}')
print(f'Minute : {datetime_IN.minute}')
@client.event 
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('--help'):
    await message.channel.send('1. -t : Tells details about present, coming period. \n2. -links : Displays links of online classes\n3. -quote : Displays a random quote\n\nBot built by Ranjul | Bot under testing | Bot has bugs :_) ')
  if message.content.startswith('-t'):
    #P1
    if (datetime_IN.hour==8 and datetime_IN.minute<59) or (datetime_IN.hour==9 and datetime_IN.minute<=10):
      print('P1')
      await message.channel.send('This is period 1, period 2 starts at 9:20')
    #P2
    elif (datetime_IN.hour==9 and datetime_IN.minute<59):
      print('P2')
      await message.channel.send('This is period 2, period 3 starts at 10:10')
    #P3
    elif (datetime_IN.hour==10 and datetime_IN.minute<50):
      print('P3')
      await message.channel.send('This is period 3, period 4 starts at 11:00')
    #P4
    elif (datetime_IN.hour==11 and datetime_IN.minute<49):
      print('P4')
      await message.channel.send('This is period 4, period 5 starts at 11:50')
    #P5
    elif (datetime_IN.hour==11 and datetime_IN.minute<59) or (datetime_IN.hour==12 and datetime_IN.minute<=30):
      print('P5')
      await message.channel.send('This is period 5, period 6 starts at 12:40')
    #P6
    elif (datetime_IN.hour==12 and datetime_IN.minute>=40) or (datetime_IN.hour==13 and datetime_IN.minute<=20):
      print('P6')
      await message.channel.send('This is the last period :)')
    #else:
      await message.channel.send('There are no active classes now')       
  

  if message.content.startswith('-links'):
    os = db["OS"]
    gt = db["GT"]
    coa = db["COA"]
    ethics = db["Ethics"]
    consti = db["Constitution"]
    dbms = db["DBMS"]
    os_lab = db["OS_Lab"]
    dig_lab = db["Digital_Lab"]
    minor = db["Minor"]
    honors = db["Honors"]
    await message.channel.send(f'OS: {os}\nGT: {gt}\nCOA: {coa}\nEthics: {ethics}\nConstitution: {consti}\nDBMS: {dbms}\nOS_Lab: {os_lab}\nDigital_Lab: {dig_lab}\nMinor: {minor}\nHonors: {honors}\n')
  if message.content.startswith('-quote'):
    q=get_quote()
    await message.channel.send(q)

keep_alive()
client.run(os.environ['TOKEN'])



