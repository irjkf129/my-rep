import discord
from discord import user
from discord.ext.commands import Bot
import asyncio


 
TOKEN = 'NjEzNDY3NTkwODk5MjY5Njk1.XVxYqg.hgWWeSORNQ1tt2UpHmGiqkyM1yA'


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('!spam'):
        if message.author.name=='Alternat1va':
            for i in message.guild.members:
                if not i.bot:
                    await i.send("""Привет.
Поверь, если ты потратишь буквально 2-е минуты на прочтение этого месседжа, то оно обеспечит тебе минимум месяц супер-лампового общения с людьми, со схожими интересами.
Так что я считаю, что тебе будет только на руку, если ты потратишь эти самые 120 секунд, и обеспечишь себя дружеским теплом.
У нас имеется даже чат, созданный специально для того, чтобы люди увидили тебя, и захотели с тобой познакомиться. Чат называется "чатик", и как я написал выше, этот чат создан специально для тебя.
Так что я буду крайне признателен, если ты всё-же начнёшь общаться с участниками нашего сообщества, и наконец-таки найдёшь лд. https://discord.gg/MVA7zRG
""")
client.run(TOKEN)

