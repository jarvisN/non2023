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

bot = commands.Bot(command_prefix='!')



@bot.command()
async def hello(ctx):
    """Says hello to the user"""
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


if __name__ == '__main__':
    bot.run('MTA4OTc5ODk2NDgxNzE3ODc0NQ.GgUZW5._dJUD8p0q7TGn2upX9ybiygUfj5UPGrwu0dJkg')
