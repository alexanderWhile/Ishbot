import os

import discord
import random 
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/i ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the {member.guild} server! My name is Ishbot, your humble servant.'
    )


@bot.command(name = 'roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides +1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name = 'who_is_a_good_boy', help='Returns who is a good boy.')
async def who_is_a_good_boi(ctx):
    await ctx.send('*barks happily*')

bot.run(TOKEN)
