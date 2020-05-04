import os
import asyncio

import discord
import random 
from dotenv import load_dotenv
import xdice
import traceback

from discord.ext import commands

import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='<:IshBot:704803379452313710> ')

def find_rolls(s):
    inside = False
    matches = []
    # split on whitespace
    # split on the empty space adjacent to $$'s.
    for tok in re.split(r'\s+|(?<=\$\$)(?=\S)|(?<=\S)(?=\$\$)', s):
        if re.match(r'\S*\$\$|\$\$\S*', tok):
            if inside:
                inside = False
                matches.append(" ".join(cur))
            else:
                inside = True
                cur = []
            continue

        if inside:
            cur.append(tok)

    return matches

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the {member.guild} server! My name is Ishbot, your humble servant.'
    )


@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, d):
    try:
        result = xdice.roll(d)
        await ctx.send(result)
    except:
        await ctx.send("I don't understand what you want me to do.")
        traceback.print_exc()


@bot.command(name='blackjack', help='Play a game of Blackjack with Ishbot!')
async def deal(ctx):
    await ctx.send("I don't know how to play that yet, but I will soon!")


@bot.command(name='hookers', help="Wouldn't you like to know?")
async def hooker(ctx):
    await ctx.send("We don't have hookers just yet, sorry")


@bot.command(name='who_is_a_good_boy', help='Returns who is a good boy.')
async def who_is_a_good_boi(ctx):
    if ctx.author.nick != None:
        await ctx.send(f'*barks happily at {ctx.author.nick}*')
    else:
        await ctx.send(f'*barks happily at {ctx.author.name}*')


@bot.command(name = 'echo')
async def echo(ctx, message:str):
    print(message)



@bot.event
async def on_message(message):
    profamity_list = ['heck', 'darn', 'poop', 'frick', 'stupidhead']
    there_are_bad_words = False

    for bad_word in profamity_list:
        if bad_word in message.content:
            there_are_bad_words = True
            break

    if there_are_bad_words:
        await message.channel.send('Watch your profamity!')

    for match in find_rolls(message.content):
        result = xdice.roll("".join(match).replace(' ', ''))
        await message.channel.send("%s: %s" % (result, result.format()))

    await bot.process_commands(message)

bot.run(TOKEN)
