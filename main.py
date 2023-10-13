import discord, os
from discord import app_commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

intents.reactions = True
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.lower() == 'ratio':
        await message.add_reaction(client.get_emoji(968628253986263070))
        print("ratioed")
    elif "ratio +" in message.content.lower():
        await message.add_reaction(client.get_emoji(968628253986263070))
        print("ratioed")
    elif "+ ratio" in message.content.lower():
        await message.add_reaction(client.get_emoji(968628253986263070))
        print("ratioed")

#@client.command(name='pfp', pass_context=True)
#async def pfp(ctx):
#    picture = ctx.author.default_avatar_url


client.run(os.getenv('DISCORD_TOKEN'))

