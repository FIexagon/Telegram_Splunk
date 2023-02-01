import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection
from telethon.errors import ChannelInvalidError

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)

client.start()

# Get the channel by its username
channel_username = 'nomadsecurity'
try:
    channel = client.get_entity(channel_username)
except ChannelInvalidError:
    print(f"Invalid channel: {channel_username}")
    exit()

# Get the initial title of the channel
initial_title = channel.title
print(f"Initial title: {initial_title}")

# Monitor the channel for title changes
while True:
    channel = client.get_entity(channel)
    if channel.title != initial_title:
        initial_title = channel.title