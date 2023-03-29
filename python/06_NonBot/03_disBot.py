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
async def order(interaction: nextcord.Interaction, ticker: str, start: str, end: str, unit: str , num: str):

    print(ticker)
    print(type(ticker))
    print(start)
    print(type(start))
    print(end)
    print(unit)


    await interaction.send(f'Please wait', ephemeral=True)
    res = c.get_aggs(f"C:{ticker}, {num}, {unit}, {start}, {end}")
    # res = c.get_aggs("C:XAUUSD", 1, "day", "2023-03-22", "2023-03-24")
    print(res)


    await interaction.send(f'{res}', ephemeral=True)
    await interaction.send(f'Done', ephemeral=True)


@bot.command(name="qwerty")
async def non(aaa):

    res = c.get_aggs("C:XAUUSD", 1, "day", "2023-03-22", "2023-03-24")
    print(res)

    # create list of dictionaries containing data for each time period
    data = [{'Open': item.open, 'High': item.high, 'Low': item.low, 'Close': item.close, 'Volume': item.volume,
            'VWAP': item.vwap, 'Timestamp': item.timestamp, 'Transactions': item.transactions} for item in res]

    # create DataFrame from list of dictionaries
    df = pd.DataFrame(data)

    # print the resulting DataFrame
    print(df)


    # Format the DataFrame using tabulate
    table = tabulate(df, headers='keys', tablefmt='psql')

    # Send the table as a message using Nextcord
    await aaa.send(f'```\n{table}\n```', ephemeral=True)


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
    bot.run('MTA4OTc5ODk2NDgxNzE3ODc0NQ.GgUZW5._dJUD8p0q7TGn2upX9ybiygUfj5UPGrwu0dJkg')
