import nextcord
import time
import datetime
import pandas as pd
from tabulate import tabulate
from nextcord.ext import commands
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder


c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/')


@bot.slash_command(name="Pong!")
async def ping(ctx):
    await ctx.send('Pong!')


@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)


# @bot.slash_command(name="command")
# async def order(interaction: nextcord.Interaction, data1 ):
#     await interaction.send(f'What do you want to order? : {data1}',ephemeral=True)

@bot.slash_command(name="command")
async def order(interaction: nextcord.Interaction, ticket: str, dayStart: str, dayStop: str, unit: str):

    # get response
    res = c.get_aggs(f"C:{ticket}", 1, f"{unit}", f"{dayStart}", f"{dayStop}")

    # create list of dictionaries containing data for each time period
    data = [{'Open': item.open, 'High': item.high, 'Low': item.low, 'Close': item.close, 'Volume': item.volume, 'VWAP': item.vwap,
             'Timestamp': pd.to_datetime(item.timestamp/1000, unit='s'), 'Transactions': item.transactions} for item in res]

    # create DataFrame from list of dictionaries
    df = pd.DataFrame(data)

    # Convert the DataFrame to a string
    df_string = df.to_string()

    # Format the DataFrame using tabulate
    table = tabulate(df, headers='keys', tablefmt='psql')

    print(f'```\n{table}\n```')
    
    await interaction.send(f'```\n{table}\n```')


@bot.slash_command(name="non")
async def non(interaction: nextcord.Interaction, data1: str, data2: str):

    print(len(data2))
    await interaction.send(f"ok test!", ephemeral=True)


# @bot.slash_command(name="test")
# async def test(interaction: nextcord.Interaction,):
#     await interaction.send('Pong!')
#     import pandas as pd

#     # Create a sample DataFrame
#     df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

#     # # Convert the DataFrame to a string
#     # df_string = df.to_string()

#    # Format the DataFrame using tabulate
#     table = tabulate(df, headers='keys', tablefmt='psql')

#     # Send the table as a message using Nextcord
#     await interaction.send(f'```\n{table}\n```')


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


if __name__ == '__main__':
    bot.run('MMTA4OTc5ODk2NDgxNzE3ODc0NQ.GkLCVv.EfR8otdXaLYdRSnHMjlMNRKnLoyPWydQvq72zs')
