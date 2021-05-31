import random

import discord
from discord.ext import commands
import asyncio

import details
from Commands import quotes
from Commands import links
from Commands import time
from Commands import wish_good
from Commands.ask import ask_qn
from Commands import stupid_bot
from Commands import random_events
from Commands import encourage
from Commands import bot_info
from Commands import mute

prefix = details.server_prefix
token = details.token
rickroll = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)


@client.event
async def on_ready():
    print(f'{client.user} is online!')
    await client.change_presence(activity=discord.Streaming(name=f'{details.server_prefix}help', url=rickroll))


@client.command()
async def hello(ctx):
    await ctx.reply('Hello!')


@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping_time = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong! `Latency: {int(ping_time)}ms`")


@client.command()
async def userid(ctx, target: discord.Member = None):
    if target:
        await ctx.reply(target.id)
    else:
        await ctx.reply(ctx.author.id)


@client.command()
async def inspire(ctx):
    await ctx.send(quotes.get_quote())


@client.command()
async def link(ctx, link):
    if link.lower() == 'list':
        await ctx.send(links.link_list())
    else:
        await ctx.send(links.link_message(link))


@client.command()
async def goodmorning(ctx):
    await ctx.send(wish_good.good_morning(ctx.message.content, ctx))


@client.command()
async def goodafternoon(ctx):
    await ctx.send(wish_good.good_afternoon(ctx.message.content, ctx))


@client.command()
async def goodevening(ctx):
    await ctx.send(wish_good.good_evening(ctx.message.content, ctx))


@client.command()
async def goodnight(ctx):
    await ctx.send(wish_good.good_night(ctx.message.content, ctx))


@client.command(aliases=['flip'])
async def flip_command(ctx):
    await ctx.reply(random_events.coin_flip())


@client.command()
async def ask(ctx):
    await ctx.reply(ask_qn(ctx.message.content))


@client.command()
async def roll(ctx):
    await ctx.reply(random_events.roll_dice())


@client.command()
async def bot_bio(ctx):
    await ctx.reply(bot_info.bot_bio)


@client.command()
async def help(ctx):
    embed = bot_info.bot_help()
    await ctx.send(embed=embed)


@client.command(aliases=['mute'])
async def mute_func(ctx, member: discord.Member, time=None):
    if ctx.author.guild_permissions.manage_roles:
        role = discord.utils.get(ctx.guild.roles, name="muted")
        roles_list = member.roles
        await member.remove_roles(*roles_list[1:])
        await member.add_roles(role)
        if time is not None:
            await ctx.reply(f'{member} has been muted for {time}')
            await asyncio.sleep(mute.get_time(time))
            await member.remove_roles(role)
            await member.add_roles(*roles_list[1:])
            await ctx.send(f'{member} has been unmuted.')
        else:
            await ctx.reply(f'{member} has been muted')


@client.event
async def on_message(message):
    msg = message.content.lower()

    if message.author == client.user:
        return
    if len(msg.split()) == 1:
        if msg in ['sparkle', 'sparkles']:
            await message.reply('✨')
    else:
        if any(word in msg for word in [' sparkle', 'sparkle ', ' sparkles', 'sparkles ']):
            await message.reply('✨')
    await client.process_commands(message)

    if msg.startswith(f'{prefix}time'):
        await message.reply(time.time_bm(msg))

    if any(word in msg for word in stupid_bot.stupid_bot) and any(word in msg for word in stupid_bot.bot_call):
        if any(word not in msg for word in stupid_bot.stupid_exception):
            await message.reply(random.choice(stupid_bot.stupid_bot_revenge))

    if any(word in msg for word in ['845225811152732179']):  # respond to pings
        if not any(word in msg for word in stupid_bot.stupid_bot):
            await message.reply('I heard my name. what\'s up ?')

    if any(word in msg for word in encourage.sad_words):  # encourages you if you type a sad message
        if any(word in msg for word in ['I', 'i', 'im']):
            if not any(word in msg for word in ['not']):
                await message.reply(random.choice(encourage.encouragement))


if __name__ == '__main__':
    client.run(token)
