import nextcord
from nextcord.ext import commands

TESTING_GUILD_ID = 123456789  # Replace with your guild ID
# the prefix is not used in this example

intents = nextcord.Intents.default()
intents.members = True
command_prefix = '/'
bot = commands.Bot(command_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.slash_command(name="non")
async def non(interaction: nextcord.Interaction, data1: str, data2: str):

    print(len(data2))
    await interaction.send(f"ok test!", ephemeral=True)

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")


if __name__ == '__main__':
    bot.run('MTA4OTc5ODk2NDgxNzE3ODc0NQ.GHKiJR.dvE7HzYCjn_0R5nq5MfWdrbmPpyLnSeBm_4Y54')
