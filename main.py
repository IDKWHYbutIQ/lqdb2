import discord
import os
from discord.utils import DISCORD_EPOCH
import requests
import json
from server import gotchu
import asyncio


intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
client = discord.client


@bot.event
async def on_message(msg): 
  if msg.author.id == 440849314487468032: 
    await msg.channel.send("stfu <@440849314487468032>")
  
  
  if "pls" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('pls hurt me mommy')


  if "uwu" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('npc')

  if "sorry" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('no')

  if "real" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('REALITÄTSNAH.')

  if "yes" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('no')

  if "lol" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send(':(')

  if "@516683370768498719" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('he busy') 

  if "ty" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('yw')

  if "ez" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('EEEEZzzZZZ <@699913010969575537> STILL HARDSTUCK LMAOOAOAO')
    
  if "why" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('cuz yo booty stank') 

  if "hi" in msg.content:
    if msg.author == bot.user:
      return
    await msg.channel.send('hola, how are u')

  if "good" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('kys <:troll:740142798677868565>')

  if "wtf" in msg.content: 
    if msg.author == bot.user:
      return
    await msg.channel.send('https://tenor.com/view/nope-scared-imout-gif-9341104105491691995')

  if "kys" in msg.content:
    if msg.author == bot.user:
      return
    await msg.channel.send('169.82.111.118 RAAAAAAAAAAAAAAAAAAAH')




    


    
      
    

  

  
  
  
 


gotchu()
  


bot.run(os.environ['DISCORD_TOKEN'])