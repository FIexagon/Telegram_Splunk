import json
import sys
sys.path.append(os.path.join(os.environ['SPLUNK_HOME'],'etc','apps','Telegram-chanel','bin')) #build local path and add it to the python path so we can load modules, hack!

# классы для работы с API Telegram
from telethon.sync import TelegramClient
from telethon import connection
from telethon.errors import ChannelInvalidError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# запуск виртуального клиента
client = TelegramClient("fiexagon", "id", "hash")
client.start()

# получение имени канала
channel_username = 'nomadsecurity'
channel = client.get_entity(channel_username)

# передача в splunk в структуре json-файла
name = channel.title
data = {"name" : name}
data = json.dumps(data)
print(data)

client.disconnect()
