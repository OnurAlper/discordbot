from datetime import datetime
from os import getenv
from discord.ext import commands, tasks
from time import sleep
from typing import List
import discord
import asyncio
from discord import Member


intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)

bot = commands.Bot("!")


# must be utc time
STANDUP_START = (5, 0)
STANDUP_END = (6, 20)


# standup kanalının kullanıcılarını kontrol eder.
@tasks.loop(minutes=1)
async def check_standup():
    week = datetime.today().weekday()
    now = datetime.utcnow()
    # standup saati degilse bitir
    if not (now.hour == STANDUP_END[0] and now.minute == STANDUP_END[1]):
        return
    print("Checking standup")

    standup_start = now.replace(
        hour=STANDUP_START[0], minute=STANDUP_START[1], second=0, microsecond=0)

    channel = client.get_channel(int(getenv("stand_up")))
    # son 100 mesaji al
    message_history = await channel.history(limit=100).flatten()

    mesaj_atanlar = []
    for message in message_history:
        # standup saatinden 10 dakika oncesine kadar degilse bitir
        if message.created_at < standup_start:
            break

        # bot ise gec
        if message.author.bot:
            continue

        mesaj_atanlar.append(message.author.id)
    #guild = client.get_guild(int(getenv("guild")))
    members: List[Member] = []
    for member in channel.members:
        if 'developer' in [role.name for role in member.roles]:
            members.append(member.id)
    # mesaj atanlari filtrele
    mesaj_atmayanlar = list(set(members) - set(mesaj_atanlar))

    # mesaj atmayanlara mesaj gonder
    message = ' '.join(f'<@{user_}>' for user_ in mesaj_atmayanlar)
    message += " lütfen günlük standup'ı unutmayınız."
    if week <= 4:  # Haftaiçi ve Haftasonu gönderilecek mesajlar
        await channel.send(message)
    if week >= 5:
        print("Bugün Haftasonu")


@check_standup.before_loop
async def before():
    await client.wait_until_ready()

# Standup kanalına tarih basar.
@tasks.loop(minutes=1)
async def time_module():
    current_time = datetime.now().strftime("%H:%M")
    # Saat 9.10 geçe Stand-up kanalına Tarih atacak...
    if current_time == "09:00":
        # Kanal idsi girilecek.
        message_channel = client.get_channel(int(getenv("channel_id")))
        print(f"Yazdırılan kanal {message_channel}")
        weekday = datetime.today().weekday()  # Haftaiçi ve haftasonu atılacak mesajlar
        now = datetime.today()
        date_time = now.strftime("**%d/%m/%Y**")
        if weekday <= 4:  # Haftanın ilk 5 günü sürekli tarih atacak.
            await message_channel.send(date_time)



STANDUP_START = (5, 0)
STANDUP_END = (6, 20)


#  standup kanalının kullanıcılarını kontrol eder.
@tasks.loop(minutes=1)
async def bcr_check_standup():
    week = datetime.today().weekday()
    now = datetime.utcnow()
    # standup saati degilse bitir
    if not (now.hour == STANDUP_END[0] and now.minute == STANDUP_END[1]):
        return
    print("Checking standup")

    standup_start = now.replace(
        hour=STANDUP_START[0], minute=STANDUP_START[1], second=0, microsecond=0)

    channel = client.get_channel(int(getenv("channel_id")))

    # son 100 mesaji al
    message_history = await channel.history(limit=100).flatten()

    mesaj_atanlar = []
    for message in message_history:
        # standup saatinden 10 dakika oncesine kadar degilse bitir
        if message.created_at < standup_start:
            break

        # bot ise gec
        if message.author.bot:
            continue

        mesaj_atanlar.append(message.author.id)

    #guild = client.get_guild(int(getenv("guild")))
    members: List[Member] = []
    for member in channel.members:
        if 'developer' in [role.name for role in member.roles]:     
            members.append(member.id)
            if 501906258920472608 in members:
                members.remove(501906258920472608)
    # mesaj atanlari filtrele
    mesaj_atmayanlar = list(set(members) - set(mesaj_atanlar))

    # mesaj atmayanlara mesaj gonder
    message = ' '.join(f'<@{user_}>' for user_ in mesaj_atmayanlar)
    message += " lütfen günlük standup'ı unutmayınız."
    if week <= 4:  # Haftaiçi ve Haftasonu gönderilecek mesajlar
        await channel.send(message)
    if week >= 5:
        print("Bugün Haftasonu")


@bcr_check_standup.before_loop
async def before():
    await client.wait_until_ready()

# Becure haftaiçi hergün kanala tarih mesajı atacak.
@tasks.loop(minutes=1)
async def bcr_time_module():
    current_time = datetime.now().strftime("%H:%M")
    # Saat 9.10 geçe Stand-up kanalına Tarih atacak...
    if current_time == "09:00":
        # Kanal idsi girilecek.
        message_channel = client.get_channel(int(getenv("channel_id")))
        print(f"Yazdırılan kanal {message_channel}")
        weekday = datetime.today().weekday()  # Haftaiçi ve haftasonu atılacak mesajlar
        now = datetime.today()
        date_time = now.strftime("**%d/%m/%Y**")
        if weekday <= 4:  # Haftanın ilk 5 günü sürekli tarih atacak.
            await message_channel.send(date_time)


@bcr_time_module.before_loop
async def before():
    await client.wait_until_ready()
    print("Tarih Bekleniyor...")
