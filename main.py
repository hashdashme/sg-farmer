import asyncio
from discord.ext import commands, tasks
import random

#   CONFIG
token = ""  #   Search up how to get discord token.
prefix = "~"
target_channel = 00000000000000 #   Channel to run commands in.
target_bot = 668075833780469772
target_bot_prefix = "<@668075833780469772> "

print("Initalising...")

# Declare the bot, pass it a prefix and let it know to only listen to itself.
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Farming!")
    claim.start()
    await asyncio.sleep(random.uniform(60,5*60))
    daily.start()
    await asyncio.sleep(random.uniform(60, 5*60))
    arena.start()

@tasks.loop(seconds=60*60+1)
async def claim():
    channel = bot.get_channel(target_channel)
    print('Sending {}claim.'.format(target_bot_prefix))
    await channel.send('{}claim'.format(target_bot_prefix))

@tasks.loop(seconds=60*60*24+1)
async def daily():
    channel = bot.get_channel(target_channel)
    print('Sending {}daily.'.format(target_bot_prefix))
    await channel.send('{}daily'.format(target_bot_prefix))

@tasks.loop(seconds=60*60*3+60)
async def arena():
    channel = bot.get_channel(target_channel)
    print('Sending {}arena'.format(target_bot_prefix))
    await channel.send('{}arena'.format(target_bot_prefix))
    await asyncio.sleep(3)
    print('Sending 1')
    await channel.send('1')

@bot.command
async def stop(ctx):
    await ctx.message.delete()
    print('Shutting Down.')
    await bot.close()

bot.run(token, bot=False)  # Starts the bot by passing it a token and telling it it isn't really a bot. 
