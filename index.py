import requests
import asyncio
import random
import urllib.request
import sqlite3
import aiohttp
import json
import webbrowser
import googletrans
import urllib.parse
import datetime
import logging
import threading
import os
import ctypes
from random import randint
from typing import List
from googletrans import Translator
from time import perf_counter
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
from io import StringIO
from config import *
from function import *
from time import sleep, perf_counter

stop = False
client = Client('session', '27447003', '112b12886c7fe281398799ef45d80d1f')
os.system('cls')
os.system('clear')
client.start()
client.stop()

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = response.json()
usd_rate = data['Valute']['USD']['Value']
a = round(usd_rate, 2)

print('\n' + BLUE + '[' + GREEN + 'INFO' + BLUE + ']' + WHITE + ' Бот успешно запустился!\n' + BLUE + '[' + GREEN + 'INFO' + BLUE + ']' + WHITE + ' Разработчик: ' + GOLD + '@javainteger\n' + BLUE + '[' + GREEN + 'INFO' + BLUE + ']' + WHITE + ' Телеграм канал: ' + GOLD + 'https://t.me/selfcodetg' + RESET)

@client.on_message(filters.command(spam_command, prefixes=commands_prefix) & filters.me)
def spam_message_handler(client, message):
    global stop
    args = message.text.split(' ')
    message.delete()
  
    if args[1] == 'stop':
        stop = True
        client.send_message(message.chat.id, 'Вы успешно отключили спам!')
  
    else:
        i = int(args[1])
        message_text = ' '.join(args[2:])
        print(f'{BLUE}[{AQUA}LOG{BLUE}]{WHITE} Спам был успешно запущен! Кол-во сообщений: {GOLD}{i}{WHITE}')
  
        try:
            for j in range(i):
                if stop:
                    stop = False
                    break
                client.send_message(message.chat.id, message_text)
                sleep(0.67)
        except FloodWait as e:
            sleep(e.x)   

@client.on_message(filters.command(ping_command, prefixes=commands_prefix) & filters.me)
def ping_message_handler(client, message):
    start = perf_counter()
    client.edit_message_text(message.chat.id, message.id, '<b>Понг!</b>')
    end = perf_counter()
    client.edit_message_text(message.chat.id, message.id, f'<b>Понг! {round(end - start, 3)} сек.</b>')

@client.on_message(filters.command(dollar_command, prefixes=commands_prefix) & filters.me)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, '`1` Доллар [dollar] = {}₽'.format(a))

@client.on_message(filters.command(help_command, prefixes=commands_prefix) & filters.me)
def help_message_handler(client, message):
    text = """
    **Префиксы**: [.] - [/] - [!] - [-]
**Команды**: https://telegra.ph/Komandy-04-28
👨‍💻 **Разработчик:** @javainteger
    """
    client.edit_message_text(message.chat.id, message.id, text, disable_web_page_preview=True)

@client.on_message(filters.command(love_command, prefixes=commands_prefix) & filters.me)
def love_message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💖💖🤍💖💖🤍🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍🤍💖💖💖💖💖🤍🤍\n🤍🤍🤍💖💖💖🤍🤍🤍\n🤍🤍🤍🤍💖🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💌💌🤍💌💌🤍🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍🤍💌💌💌💌💌🤍🤍\n🤍🤍🤍💌💌💌🤍🤍🤍\n🤍🤍🤍🤍💌🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️\n❤️❤️❤️\n❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️\n❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️')

@client.on_message(filters.command(bulling_command, prefixes=commands_prefix) & filters.me)
async def bulling_command_handler(client, message):
    try:
        command, member, sped, kol, shabl = message.text.split()
        sped = int(sped)
        kol = int(kol)

        if shabl in ["Красивый-текст", "Провокации", "Дефолтные", "Все"]:
            with open(f"shabloni_{shabl.lower()}.txt", encoding="UTF-8") as file:
                lines = file.readlines()

            for i in range(kol):
                message_text = f"{member} " + random.choice(lines)
                await client.send_message(message.chat.id, message_text)
                await asyncio.sleep(sped)

            await message.delete()
        
        else:
            await client.send_message(message.chat.id, "Ошибка: Неправильно введено название шаблона!\nШаблоны: Красивый-текст, Провокации, Дефолтные, Все")
            await message.delete()

    except ValueError:
        await client.send_message(message.chat.id, "Ошибка: Неправильно введены аргументы!\nПример использования команды: /bulling @username 1 10 Все")
        await message.delete()

@client.on_message(filters.command(compli_command, prefixes=commands_prefix) & filters.me)
def compli_command_handler(client, message):
    txt = comp.split("\n")
    e = True
    for i in txt:
        if e == True:
            e = False
        else:
            try:
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
            except:
                pass

@client.on_message(filters.command(night_command, prefixes=commands_prefix) & filters.me)
def night_command_handler(client, message):
    txt = night.split("\n")
    e = True
    for i in txt:
        if e == True:
            e = False
        else:
            try:
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
                message.edit(f'{i}')
                sleep(1)
            except:
                pass

@client.on_message(filters.command(loves_command, prefixes=commands_prefix) & filters.me)
def loves_command_handler(client, message):
    time = 0.6
    for i in range(1):
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')   
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨✨✨✨✨''')   
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️✨✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨❤️❤️✨❤️❤️✨✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨✨❤️❤️❤️❤️❤️✨✨
✨✨✨❤️❤️❤️✨✨✨
✨✨✨✨❤️✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💚💚✨💚💚✨✨
✨💚💚💚💚💚💚💚✨
✨💚💚💚💚💚💚💚✨
✨✨💚💚💚💚💚✨✨
✨✨✨💚💚💚✨✨✨
✨✨✨✨💚✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💙💙✨💙💙✨✨
✨💙💙💙💙💙💙💙✨
✨💙💙💙💙💙💙💙✨
✨✨💙💙💙💙💙✨✨
✨✨✨💙💙💙✨✨✨
✨✨✨✨💙✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💜💜✨💜💜✨✨
✨💜💜💜💜💜💜💜✨
✨💜💜💜💜💜💜💜✨
✨✨💜💜💜💜💜✨✨
✨✨✨💜💜💜✨✨✨
✨✨✨✨💜✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🤍🤍✨🤍🤍✨✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨✨🤍🤍🤍🤍🤍✨✨
✨✨✨🤍🤍🤍✨✨✨
✨✨✨✨🤍✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🖤🖤✨🖤🖤✨✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨✨🖤🖤🖤🖤🖤✨✨
✨✨✨🖤🖤🖤✨✨✨
✨✨✨✨🖤✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💛💛✨💛💛✨✨
✨💛💛💛💛💛💛💛✨
✨💛💛💛💛💛💛💛✨
✨✨💛💛💛💛💛✨✨
✨✨✨💛💛💛✨✨✨
✨✨✨✨💛✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        message.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🧡🧡✨🧡🧡✨✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨✨🧡🧡🧡🧡🧡✨✨
✨✨✨🧡🧡🧡✨✨✨
✨✨✨✨🧡✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(3)

@client.on_message(filters.command(like_command, prefixes=commands_prefix) & filters.me)
def like_command_handler(client, message):
    time = 0.6
    for i in range(1):
        message.edit(f'''      
🟦''')   
        sleep(0.001)
        message.edit(f'''
🟦🟦''')   
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(5)

@client.on_message(filters.command(dislike_command, prefixes=commands_prefix) & filters.me)
def dislike_command_handler(client, message):
    time = 0.6
    for i in range(1):
        message.edit(f'''
🟥''')   
        sleep(0.001)
        message.edit(f'''
🟥🟥''')   
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(1)
        message.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(1)
        message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
        sleep(1)
        message.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(4)

@client.on_message(filters.command(profile_command, prefixes=commands_prefix) & filters.me)
def profile_command_handler(client, message):
    global start_date, message_count
    cursor.execute('SELECT start_date FROM relationship')
    result = cursor.fetchone()
    if result:
        start_date = datetime.datetime.strptime(result[0], "%d.%m.%Y")
    else:
        start_date = None
    
    if start_date is None:
        text = f"""💾 <b>Профиль:</b>

<b>Пользователь:</b> <code>{message.from_user.first_name}</code>
<b>Chat ID:</b> <code>{message.chat.id}</code>
<b>User ID:</b> <code>{message.from_user.id}</code>
<b>Отношения:</b> Ещё нет ❤️"""
    else:
        days = (datetime.datetime.now() - start_date).days
        messages_per_day = round(message_count / days, 2)
        text = f"""💾 <b>Профиль:</b>

<b>Пользователь:</b> <code>{message.from_user.first_name}</code>
<b>Chat ID:</b> <code>{message.chat.id}</code>
<b>User ID:</b> <code>{message.from_user.id}</code>
<b>Дата начала отношений:</b> <code>{start_date.strftime("%d.%m.%Y")}</code>
<b>Количество сообщений:</b> <code>{message_count}</code>
<b>Сообщений в день:</b> <code>{messages_per_day}</code>
<b>Дней в отношениях:</b> <code>{days}</code> ❤️"""
    client.send_message(
        message.chat.id,
        text,
        disable_web_page_preview=True,
    )

@client.on_message(filters.command(kill_command, prefixes=commands_prefix) & filters.me)
async def kill_command_handler(client, message):
    time = 1
    for i in range(1):
        await message.edit("<b>🔪 На тебя заказали убийство.</b>")
        await asyncio.sleep(3)
        await message.edit("<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")
        await asyncio.sleep(2)
        await message.edit("<b>⏳ [ 5s ]</b>")
        await asyncio.sleep(time)
        await message.edit("<b>⌛️ [ 4s ]</b>")
        await asyncio.sleep(time)
        await message.edit("<b>⏳ [ 3s ]</b>")
        await asyncio.sleep(time)
        await message.edit("<b>⌛️ [ 2s ]</b>")
        await asyncio.sleep(time)
        await message.edit("<b>⏳ [ 1s ]</b>")
        await asyncio.sleep(time)
        await message.edit("<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")
        await asyncio.sleep(time)
        await message.edit("<b>👀 Поиск.</b>")
        await asyncio.sleep(time)
        await message.edit("<b>👀 Поиск..</b>")
        await asyncio.sleep(time)
        await message.edit("<b>👀 Поиск...</b>")
        await asyncio.sleep(time)
        await message.edit("<b>👀 Поиск.</b>")
        await asyncio.sleep(time)
        await message.edit("<b>👀 Поиск..</b>")
        await asyncio.sleep(time)
        await message.edit("<b>👀 Поиск...</b>")
        await asyncio.sleep(time)
        await message.edit(random.choice(kill))
        await asyncio.sleep(5)

kill = ["<b>🔪 Убийца нашел тебя, к сожалению ты спрятался плохо и был убит</b>", "<b>⚔️Убийца не нашел тебя, вы  очень хорошо спрятались.</b>"]

@client.on_message(filters.command(type_command, prefixes=commands_prefix) & filters.me)
def type_command_handler(client, message):
    orig_text = message.text.split("type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "█"
    while (tbp != orig_text):
        try:
            message.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            message.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

@client.on_message(filters.command(drugs_command, prefixes=commands_prefix) & filters.me)
async def drugs_command_handler(client, message):
    text = f"<b>💊 Поиск запрещённых препаратов.. </b>"
    await message.edit(str(text))
    await asyncio.sleep(2)
    kilogramm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    text2 = f"<b>🚬 Найдено {random.choice(kilogramm)} кг шпека</b>"
    await message.edit(str(text2))
    await asyncio.sleep(3)
    text3 = f"<b>🌿⚗️ Оформляем вкид</b>"
    await message.edit(str(text3))
    await asyncio.sleep(5)
    drugsss = [f'<b>😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты</b>',
               f'<b>🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид</b>',
               f'<b>😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз</b>',
               f'<b>😌 Вы оформили вкид, Вам понравилось</b>']
    drug = random.choice(drugsss)
    await message.edit(drug)
    await asyncio.sleep(5)

@client.on_message(filters.command(football_command, prefixes=commands_prefix) & filters.me)
async def football_command_handler(client, message):
    time = 0.6
    for i in range(1):
        await message.edit(f"<b>⚽️ Вы зашли на футбольное поле, вам предстоит забить пенальти, чтобы победить</b>")   
        sleep(2)
        await message.edit(f"<b>⏳ Подготовка к игре.</b>")
        sleep(2)
        await message.edit(f"<b>⌛️ Подготовка к игре..</b>")
        sleep(time)
        await message.edit(f"<b>⏳ Подготовка к игре...</b>")
        sleep(time)
        await message.edit(f"<b>⚽️ Удар.</b>")
        sleep(time)
        await message.edit(f"<b>⚽️ Удар..</b>")
        sleep(time)
        await message.edit(f"<b>⚽️ Удар...</b>")
        sleep(time)
        await message.edit(random.choice(foot))
        sleep(5)

foot = ["<b>❌ К сожалению, вы проиграли..</b>", "<b>✅ Вы забили гол и победили в игре!</b>"]

@client.on_message(filters.command(random_command, prefixes=commands_prefix) & filters.me)
async def random_command_handler(client, message):
    if len(message.command) == 1:
        await message.edit("Не указан диапазон чисел.")
        return
    try:
        max_num = int(message.command[1])
    except ValueError:
        await message.edit("Некорректный аргумент.")
        return
    abobys = f'<b> Случайное число: </b>'
    too = random.randint(0, max_num)
    await message.edit(abobys + str(too))

@client.on_message(filters.command(timer_command, prefixes=commands_prefix) & filters.me)
async def timer_command_handler(client, message):
    if len(message.command) == 1:
        await message.edit("Не указано время.")
        return
    try:
        time = int(message.command[1])
    except ValueError:
        await message.edit("Некорректный аргумент.")
        return
    for i in range(time, -1, -1):
        minutes, seconds = divmod(i, 60)
        time_str = f"{minutes:02d}:{seconds:02d} ⏰"
        await message.edit(time_str)
        await asyncio.sleep(1)
    await message.edit("Время вышло! ⏰⏰⏰")

@client.on_message(filters.command(calc_command, prefixes=commands_prefix) & filters.me)
async def calc_command_handler(client, message):
    command = message.command
    if len(command) != 4:
        await message.edit("Ошибка: Некорректное количество аргументов.\nПример: /calc 2 + 3")
        return
    num1, operator, num2 = command[1:]
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        await message.edit("Ошибка: Некорректные аргументы.\nПример: /calc 2 + 3")
        return
    operators = {
        "+": ("🔥", num1 + num2),
        "-": ("❄️", num1 - num2),
        "*": ("🌟", num1 * num2),
        "/": ("💥", num1 / num2) if num2 != 0 else None
    }
    if operator not in operators:
        await message.edit("Некорректный оператор.\nПоддерживаются только +, -, *, /")
        return
    emoji, result = operators[operator]
    if result is None:
        await message.edit("Деление на ноль невозможно!")
        return
    await message.edit(f"{num1} {operator} {num2} = {result} {emoji}")

translator = Translator(service_urls=['translate.google.com'])

@client.on_message(filters.command(translate_command, prefixes=commands_prefix) & filters.me)
async def translate_command_handler(client, message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        client.edit_message_text(message.chat.id, message.id, '❌ Не указан текст для перевода.')
        return
    try:
        translated_text = translator.translate(text[1], src='auto', dest='en').text
        if len(translated_text) > 4096:
            with io.StringIO(translated_text) as file:
                chunk = file.read(4096)
                while chunk:
                    client.edit_message_text(message.chat.id, message.id, f'🌎 Перевод на английский:\n\n**{chunk}**')
                    chunk = file.read(4096)
        else:
            client.edit_message_text(message.chat.id, message.id, f'🌎 Перевод на английский:\n\n**{translated_text}**')
    except ValueError:
        client.edit_message_text(message.chat.id, message.id, '❌ Ошибка при переводе. Убедитесь, что язык поддерживается.')

@client.on_message(filters.command(weather_command, prefixes=commands_prefix) & filters.me)
async def weather_command_handler(client, message):
    
    city = message.text.split(" ")[1]
    
    url = f"https://api.weatherapi.com/v1/current.json?key=2425c17f88b04cd186a213907231404&q={city}&lang=ru"
    
    response = requests.get(url).json()
    
    location = response['location']['name']
    temp_c = response['current']['temp_c']
    feelslike_c = response['current']['feelslike_c']
    condition = response['current']['condition']['text']
    wind_kph = response['current']['wind_kph']
    wind_dir = response['current']['wind_dir']
    
    text = f"🌡 Температура в {location} сейчас: {temp_c}°C (ощущается как {feelslike_c}°C)\n"
    text += f"☁️ Текущее состояние: {condition}\n"
    text += f"💨 Скорость ветра: {wind_kph} км/ч, направление: {wind_dir}\n\n"
    
    if temp_c > 30:
        text += "🥵 Сегодня очень жарко, лучше надеть легкую одежду из натуральных материалов и не забывайте пить воду.\n"
    elif temp_c > 25:
        text += "🌞 Погода теплая, наденьте что-то лёгкое и удобное.\n"
    elif temp_c > 20:
        text += "☀️ На улице жарко, оденьте что-то легкое.\n"
    elif temp_c > 15:
        text += "🌤 Сегодня достаточно тепло, наденьте что-то лёгкое и комфортное.\n"
    elif temp_c > 10:
        text += "🌥 Сегодня прохладно, наденьте что-то теплое и комфортное.\n"
    elif temp_c > 5:
        text += "🌬 Сегодня холодно, наденьте что-то теплое, удобное и защищающее от ветра.\n"
    else:
        text += "🥶 Сегодня очень холодно, наденьте несколько слоев теплой одежды и не забудьте шапку и перчатки.\n"

    await client.edit_message_text(message.chat.id, message.id, text=text)

@client.on_message(filters.command(ipcheck_command, prefixes=commands_prefix) & filters.me)
async def ipcheck_command_handler(client, message):
  ip = message.text.split(" ")[1]
  
  url = f"http://ip-api.com/json/{ip}"
  
  response = requests.get(url).json()
  
  text = f"👤 IP-адрес: {response['query']}\n"
  text += f"📍 Местоположение: {response['city']}, {response['region']}, {response['country']} ({response['countryCode']})\n"
  text += f"🌎 Широта/долгота: {response['lat']}/{response['lon']}\n"
  text += f"🕰️ Часовой пояс: {response['timezone']}\n"
  text += f"🌐 Провайдер: {response['isp']}\n"

  await message.reply(text)

@client.on_message(filters.command("resolve", prefixes=commands_prefix) & filters.me)
async def resolve_domain_command_handler(client, message):
    server = message.text.split()[1]
    url = f"https://api.mcsrvstat.us/2/{server}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.json()
    players = f"👥 Игроки: {response.get('players', {}).get('online', 0)}/{response.get('players', {}).get('max', 0)}\n"
    version = f"🌐 Версия: {response.get('version', 'неизвестно')}\n"
    motd = f"💬 MOTD: {response.get('motd', {}).get('clean', [''])[0]}\n"
    text = f"📡 Сервер: {response.get('ip', server)}:{response.get('port', 25565)}\n{players}{version}{motd}"
    text += "🟢 Сервер в сети!\n" if response.get('online') else "🔴 Сервер не в сети.\n"
    await message.reply(text)

@client.on_message(filters.command(dictionary_command, prefixes=commands_prefix) & filters.me)
async def dictionary_command_handler(client, message):
    word = message.text.split()[1].lower()

    api_key = 'dict.1.1.20230415T085245Z.578fe74ec51ae91c.daee8b2a6c12fd3435c2f7193971b4b7d093b83c'
    url = f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={api_key}&lang=en-ru&text={word}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'def' in data:
            text = f"📕 <b>{word.capitalize()}</b>:\n"
            for i, definition in enumerate(data['def'][0]['tr']):
                text += f"{i+1}. {definition['text']}\n"
        else:
            text = f"⚠️ <b>Слово '{word}' не найдено в словаре</b>"
    except:
        text = f"❌ <b>Произошла ошибка при обработке запроса</b>"

    await client.edit_message_text(message.chat.id, message.id, text=text)

@client.on_message(filters.command(write_command, prefixes=commands_prefix) & filters.me)
async def write_command_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Введите текст")
    m = await message.reply_text("Печатает...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Загрузка...")
    await m.delete()
    await message.reply_photo(hand)

@client.on_message(filters.command(python_command, prefixes=commands_prefix) & filters.me)
def python_command_handler(client, message):
    _, name, *code = message.text.split()
    code = "\n".join(code)

    with open(f"{name}.py", "w") as f:
        f.write(code)

    client.edit_message_text(message.chat.id, message.id, f"Файл {name}.py успешно записан! ✅")
    with open(f"{name}.py", "rb") as f:
        client.send_document(message.chat.id, document=f, caption=f"{name}.py")

    os.remove(f"{name}.py")

@client.on_message(filters.text & ~filters.me)
def message_handler(client, message):
    global message_count, start_date
    if start_date is not None:
        message_count += 1

start_date = None
message_count = 0

conn = sqlite3.connect('bot_data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS relationship
                  (id integer primary key, start_date text)''')
conn.commit()

conn = sqlite3.connect('bot_data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS relationship
                  (id integer primary key, start_date text)''')
conn.commit()

@client.on_message(filters.command(relationship_command, prefixes=commands_prefix) & filters.me)
def relationship_command_handler(client, message):
    global start_date, message_count
    args = message.text.split(" ")
    cursor.execute('SELECT start_date FROM relationship')
    results = cursor.fetchall()

    if len(results) > 0:
        client.send_message(
            message.chat.id,
            "🚫 Вы уже в отношениях. 🚫",
        )
    elif len(args) == 2:
        try:
            start_date = datetime.datetime.strptime(args[1], "%d.%m.%Y")
            cursor.execute('INSERT INTO relationship(start_date) VALUES (?)', (args[1],))
            conn.commit()
            message_count = 0
            client.send_message(
                message.chat.id,
                "👩‍❤️‍👨 Отношения начались {}! ❤️\nНапишите /profile, чтобы увидеть информацию о нашем профиле.".format(
                    start_date.strftime("%d.%m.%Y")
                ),
            )
        except ValueError:
            client.send_message(
                message.chat.id,
                "🚫 Неправильный формат даты. Введите дату в формате dd.mm.yyyy.",
            )
    else:
        client.send_message(
            message.chat.id,
            "🚫 Неправильный формат команды. Введите команду в формате /relationship dd.mm.yyyy.",
        )

@client.on_message(filters.command(information_command, prefixes=commands_prefix) & filters.me)
async def information_message_handler(client, message):
    username = message.text.split(f'{message.command[0]} ')[-1]
    user = await client.get_users(username)
    if user:
        first_name = user.first_name if user.first_name else '❌'
        last_name = user.last_name if user.last_name else '❌'
        mention = user.mention if user.mention else '❌'
        is_scam = '✅' if hasattr(user, 'is_scam') and user.is_scam else '❌'
        is_premium = '✅' if hasattr(user, 'is_premium') and user.is_premium else '❌'
        language_code = user.language_code if hasattr(user, 'language_code') else '❌'
        emoji_status = user.emoji_status if hasattr(user, 'emoji_status') else '❌'
        phone_number = user.phone_number if hasattr(user, 'phone_number') else '❌'
        text = f'👤 Имя: {first_name}\n👥 Фамилия: {last_name}\n📌 Упоминание: {mention}\n❗️ Scam: {is_scam}\n💎 Telegram Premium: {is_premium}\n🌐 Язык: {language_code}\n😀 Эмодзи статус: {emoji_status}\n☎️ Телефон: {phone_number}'
        await client.send_message(message.chat.id, text)
    else:
        await client.send_message(message.chat.id, f'Пользователь {username} не найден')

@client.on_message(filters.command(phone_command, prefixes=commands_prefix) & filters.me)
async def phone_message_handler(client, message):

    phone_number = message.text.split()[1]

    info = phone_info(phone_number)

    if info[0] == 'Телефон не найден':
        message_text = f"📱 Информация о номере телефона **{phone_number}**:\n\n{info[0]}"
    else:
        message_text = f"📱 Информация о номере телефона **{phone_number}**:\n\n🌍 Страна: {info[2]}\n📍 Регион: {info[0]}\n🏠 Округ: {info[3]}\n🌐 Язык: {info[4]}\n👨‍💼 Оператор: {info[1]}"

    await client.send_message(
        chat_id=message.chat.id,
        text=message_text,
    )

@client.on_message(filters.command(xyu_command, prefixes=commands_prefix) & filters.me)
async def xuy_message_handler(client, message):
    await message.edit(f'''<b>🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆</b>''')

@client.on_message(filters.command(mother_command, prefixes=commands_prefix) & filters.me)
async def mother_message_handler(client, message):
    selfcode1 = [f"<b>✅ МАМАША НАЙДЕНА</b>"]
    selfcode = [f"<b>❌ Мамаша не найдена</b>"]
    await message.edit("<b>🔍 Поиск твоей мамки начался...</b>")
    await message.edit("<b>🔍 Ищем твою мамашу на Авито...</b>")
    await asyncio.sleep(3)
    text = random.choice(selfcode)
    await message.edit(text)
    await message.edit("<b>🔍 Поиск твоей мамаши на свалке...</b>")
    await asyncio.sleep(3.0)
    text = random.choice(selfcode1)
    await message.edit(text)
    await asyncio.sleep(5.0)

@client.on_message(filters.command(message_command, prefixes=commands_prefix) & filters.me)
async def message_message_handler(client, message):
    args = message.text.split(maxsplit=2)[1:]
    delay = args[0].split()
    text = args[1]
    delay_seconds = 0
    
    for d in delay:
        if d.endswith("ч"):
            delay_seconds += int(d[:-1]) * 3600
        elif d.endswith("м"):
            delay_seconds += int(d[:-1]) * 60
        elif d.endswith("с"):
            delay_seconds += int(d[:-1])
    
    await asyncio.sleep(delay_seconds)
    await client.send_message(message.chat.id, text)

@client.on_message(filters.command(hug_command, prefixes=commands_prefix) & filters.me)
async def hug_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно обнять.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/hug/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} обнял(а) {user.mention}.")

@client.on_message(filters.command(kiss_command, prefixes=commands_prefix) & filters.me)
async def kiss_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно поцеловать.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/kiss/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} поцеловал(а) {user.mention}.")

@client.on_message(filters.command(hit_command, prefixes=commands_prefix) & filters.me)
async def hit_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно ударить.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/hit/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} ударил(а) {user.mention}.")

@client.on_message(filters.command(bite_command, prefixes=commands_prefix) & filters.me)
async def bite_message_handler(client, message):
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.edit_text("Необходимо ответить на сообщение пользователя, которого нужно укусить.")
        return
    user = reply_msg.from_user
    first_name = message.from_user.first_name
    random_gif = f"gifs/bite/{random.randint(1, 10)}.gif"
    try:
        await client.send_animation(
            chat_id=message.chat.id,
            animation=random_gif,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        logging.exception(e)
        await message.edit_text("Не удалось отправить gif.")
        return
    await message.edit_text(f"{first_name} укусил(а) {user.mention}.")

@client.on_message(filters.command(gay_command, prefixes=commands_prefix) & filters.me)
async def gay_message_handler(client, message):
    percent = random.randint(1, 100)
    response_text = f"Ты на {percent}% гей 🏳️‍🌈"
    await message.edit_text(response_text)

@client.on_message(filters.command(penis_command, prefixes=commands_prefix) & filters.me)
async def penis_message_handler(client, message):
    pensil = random.randint(1, 30)
    response_text = f"Твой член равен = {pensil}см 😏"
    await message.edit_text(response_text)

@client.on_message(filters.command(article_command, prefixes=commands_prefix) & filters.me)
async def article_message_handler(client, message):
    articles = ["Статья 148. Неуклонное нарушение правил дорожного движения - 30 дней тюрьмы",
                "Статья 282.1. Пропаганда ненависти, вражды или унижение человеческого достоинства - 2 года условно",
                "Статья 127.2. Нарушение авторских и смежных прав - 3 года ограничения свободы",
                "Статья 132. Безумство - бессрочное содержание в психиатрической лечебнице",
                "Статья 159.4. Мошенничество с использованием электронных и информационных технологий - 5 лет лишения свободы"
                "Статья 105. Убийство - от 6 до 15 лет лишения свободы",
                "Статья 112. Умышленное причинение тяжкого вреда здоровью - до 10 лет лишения свободы",
                "Статья 118. Умышленное причинение средней тяжести вреда здоровью - до 5 лет лишения свободы",
                "Статья 127.1. Нарушение авторских прав - до 5 лет лишения свободы",
                "Статья 129. Хищение - до 10 лет лишения свободы",
                "Статья 132.1. Насилие в семье - от 2 до 5 лет лишения свободы",
                "Статья 136.1. Легковая наркомания - до 2 лет исправительных работ",
                "Статья 146. Нарушение автомобильных правил - до 2 лет лишения свободы",
                "Статья 161. Нарушение авторских прав в Интернете - до 5 лет лишения свободы",
                "Статья 162. Оскорбление - до 1 года ограничения свободы",
                "Статья 163. Клевета - до 6 месяцев ограничения свободы"]

    article = random.choice(articles)

    await message.edit_text(f"📕 **Моя статья УК РФ:**\n {article}")

@client.on_message(filters.command(dice_command, prefixes=commands_prefix) & filters.me)
async def dice_command_handler(client, message):
    
    number = randint(1, 6)
    
    await message.edit(f"🎲 {number}")

@client.on_message(filters.command(loved_command, prefixes=commands_prefix) & filters.me)
async def loved_message_handler(client, message):
    animation = [
        '❤️', '🧡❤️', '💛🧡❤️', '💚💛🧡❤️', '💙💚💛🧡❤️', '💜💙💚💛🧡❤️', '🤍💜💙💚💛🧡❤️', 
        '❤️🤍💜💙💚💛🧡', '🧡❤️🤍💜💙💚💛', '💛🧡❤️🤍💜💙💚', '💚💛🧡❤️🤍💜💙', '💙💚💛🧡❤️🤍💜', 
        '💜💙💚💛🧡❤️🤍', '🤍💜💙💚💛🧡❤️', '❤️🤍💜💙💚💛', '🧡❤️🤍💜💙💚', '💛🧡❤️🤍💜💙',
        '💚💛🧡❤️🤍💜', '💙💚💛🧡❤️🤍', '💜💙💚💛🧡❤️', '🤍💜💙💚💛', '❤️🤍💜💙💚', 
        '🧡❤️🤍💜💙', '💛🧡❤️🤍💜', '💚💛🧡❤️🤍', '💙💚💛🧡❤️', '💜💙💚💛🧡', '❤️🤍💜💙💚', 
        '🧡❤️🤍💜💙', '💛🧡❤️🤍💜', '💚💛🧡❤️🤍', '💙💚💛🧡', '💜💙💚💛', '🤍💜💙💚', '❤️🤍💜💙', 
        '🧡❤️🤍💜', '💛🧡❤️🤍', '💚💛🧡', '💙💚', '💜'
    ]
    
    for i in range(2):
        for heart in animation:
            await asyncio.sleep(0.5)
            await message.edit(heart)

async def ship(client, message, girl: str, boy: str):
    if not girl or not boy:
        await message.edit("🚫 Необходимо указать имена девушки и парня.\nПример команды: **/lovestory Анна Дмитрий**")
        return

    animation = [
        f"💖 {girl} любит {boy} 💖",
        f"💕 {girl} и {boy} навсегда вместе 💕",
        f"💘 {girl} и {boy} созданы друг для друга 💘",
        f"💓 Любовь витает в воздухе между {girl} и {boy} 💓",
        f"💝 {boy} заставляет сердце {girl} биться чаще 💝",
        f"❤️‍🔥 {boy} очень сильно любит {girl} ❤️‍🔥",
    ]

    for text in animation:
        await message.edit(text)
        await asyncio.sleep(3)

    await message.edit(f"🎉 {girl} и {boy} официально вместе! 🎉")

    await message.reply("❤️❤️🧡💛💚💙💜❤️❤️")


@client.on_message(filters.command(lovestory_command, prefixes=commands_prefix) & filters.me)
async def lovestory_message_handler(client, message):
    try:
        girl, boy = message.text.split()[1:]
    except ValueError:
        await message.edit("🚫 Необходимо указать имена девушки и парня.\nПример команды: **/lovestory Анна Дмитрий**")
        return

    anim_msg = await message.reply("🚢 Создаем историю любви... 🚢")
    
    await asyncio.sleep(3)

    await ship(client, anim_msg, girl, boy)

async def escape(client, message):
    good_ending_animation = [
        "🏃‍♀️ Ты убегаешь от маньяка. 🏃‍♀️",
        "🚶‍♀️ Он поблизости. 🚶‍♀️",
        "🏃‍♀️ Ты ускоряешь шаги. 🏃‍♀️",
        "🏃‍♀️ Он с каждой секундой приближается. 🏃‍♀️",
        "🏃‍♀️ Ты бежишь и видишь свет. 🏃‍♀️",
        "🙏 Ты кричишь \"Помогите!\". 🙏",
        "👨‍👩‍👧‍👦 Семья слышит и бежит на помощь. 👨‍👩‍👧‍👦",
        "🎉 Ты сбежала от маньяка! 🎉",
        "😅 Руки и ноги дрожат от испуга. 😅",
    ]

    bad_ending_animation = [
        "🏃‍♀️ Ты убегаешь от маньяка. 🏃‍♀️",
        "🚶‍♀️ Он поблизости. 🚶‍♀️",
        "🏃‍♀️ Ты ускоряешь шаги. 🏃‍♀️",
        "🏃‍♀️ Он с каждой секундой приближается. 🏃‍♀️",
        "🏃‍♀️ Ты продолжаешь бежать, но устаешь. 🏃‍♀️",
        "🏃‍♀️ Он тебя догнал... ☠️",
    ]

    ending_type = random.choice(['good', 'bad'])

    for text in good_ending_animation if ending_type == 'good' else bad_ending_animation:
        await message.edit(text)
        await asyncio.sleep(3)

    await message.edit("🚨 Ты в безопасности! 🚨" if ending_type == 'good' else "☠️ Маньяк поймал тебя... ☠️")

@client.on_message(filters.command(escape_command, prefixes=commands_prefix) & filters.me)
async def escape_message_handler(client, message):
    anim_msg = await message.reply("🏃‍♀️ Начинаем побег от маньяка... 🏃‍♀️")
    await asyncio.sleep(3)
    await escape(client, anim_msg)


@client.on_message(filters.command(crypto_command, prefixes=commands_prefix) & filters.me)
async def crypto_message_handler(client, message):
    crypto_info = crypto()
    await message.reply(crypto_info)

client.run()
