import nextcord
from nextcord.ext import commands

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

    

@bot.slash_command(name="command")
async def order(interaction: nextcord.Interaction, data1 ):
    await interaction.send(f'What do you want to order? : {data1}',ephemeral=True)


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


if __name__ == '__main__':
    bot.run('MTA4OTc5ODk2NDgxNzE3ODc0NQ.GOEICC.BcEcsytgxYcka-_Ljb16XvXY9JYlvijMgK5VC4')
