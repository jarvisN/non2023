import nextcord
from nextcord.ext import commands
import requests
import json


Token = 'MTA4OTc5ODk2NDgxNzE3ODc0NQ.G5L-W3.Lk54axG2t9tQSd3CzYEQE6hVcrsh4k-c87SwmQ'


intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/')
# bot = commands.Bot()


@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):

    await interaction.send("Pong4!", ephemeral=True)

# ==================== Test Zone : Start ====================

# @bot.slash_command(name="aaa")
# async def non1(interaction: nextcord.Interaction, data1: str, data2: str):

#     await interaction.send(f"ok aaa!", ephemeral=True)

# @bot.slash_command(name="bbb")
# async def non2(interaction: nextcord.Interaction, data1: str):

#     await interaction.send(f"ok bbb!", ephemeral=True)


# @bot.slash_command(name="ddd")
# async def non2(interaction: nextcord.Interaction, data3: str):
#     await interaction.send(f'test')
#     # await interaction.send(f"ok ddd!", ephemeral=True)

# @bot.slash_command(name="eee")
# async def non2(interaction: nextcord.Interaction, data3: str):

#     url = 'http://127.0.0.1:5000/'

#     response = requests.get(url)
#     print(response.text)

#     await interaction.send(f'{response.text}')

# @bot.slash_command(name="fff")
# async def non2(interaction: nextcord.Interaction, data3: str):

#     payload = {'key1': 'test', 'key2': data3}
#     headers = {'content-type': 'application/json'}
#     url = 'http://127.0.0.1:5000/myapi'

#     response = requests.post(url, data=json.dumps(payload), headers=headers)
#     print(response.text)

#     await interaction.send(f'{response.text}')
    
    
# @bot.slash_command(name="ggg")
# async def non2(interaction: nextcord.Interaction, data3: str):

  
#     url = 'http://127.0.0.1:5000/test'

#     response = requests.get(url)
#     print(response.text)

#     await interaction.send(f'{response.text}')
    
    
# @bot.slash_command(name="hhh")
# async def non2(interaction: nextcord.Interaction, data1: str, data2: str, data3: str, data4: str):

#     payload = {'Ticket': data1, 'DayStart': data2,'DayStop' : data3,'UniT' : data4}
#     headers = {'content-type': 'application/json'}
#     url = 'http://127.0.0.1:5000/myapi'

#     response = requests.post(url, data=json.dumps(payload), headers=headers)
#     print(response.text)

#     await interaction.send(f'{response.text}')
    
# @bot.slash_command(name="iii")
# async def non2(interaction: nextcord.Interaction, ticket: str, start: str, to: str, unit: str):

#     payload = {'Ticket': ticket.upper(), 'DayStart': start,'DayStop' : to,'UniT' : unit}
#     headers = {'content-type': 'application/json'}
#     url = 'http://127.0.0.1:5000/test'

#     response = requests.post(url, data=json.dumps(payload), headers=headers)
#     print(response.text)

#     await interaction.send(f'{response.text}')

# ==================== Test Zone : End ====================
    
@bot.slash_command(name="price")
async def non2(interaction: nextcord.Interaction, ticket: str, start: str, to: str, unit: str):

    payload = {'Ticket': ticket.upper(), 'DayStart': start,'DayStop' : to,'UniT' : unit}
    headers = {'content-type': 'application/json'}
    url = 'http://127.0.0.1:5000/ask'

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)

    await interaction.send(f'{response.text}')
    
@bot.slash_command(name="jjj")
async def test(interaction: nextcord.Interaction,test:str,description="test"):
    await interaction.send(f'test description')
    
@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


if __name__ == '__main__':
    bot.run(Token)