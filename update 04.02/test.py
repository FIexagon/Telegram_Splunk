import json
import sys
import requests as req

sys.path.append('/usr/bin/python3.8')
sys.path.append('/usr/lib/python3.8')
sys.path.append('/usr/local/lib/python3.8/dist-packages')

# классы для работы с API Telegram
from telethon.sync import TelegramClient
from telethon import connection
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.sessions import StringSession
def main():
 # запуск виртуального клиента
 string = '<строковый клиент>
 client = TelegramClient(StringSession(string), "<id>", "<hash>")
 client.start()

 #получение информации о последнем сообщении
 requestURL = "https://api.telegram.org/bot<token>/getUpdates"
 response = req.get(url=requestURL)
 updates = response.json()

 name = updates['result'][-1]['channel_post']['sender_chat']['username']		#получение актуальной ссылки на канал

 channel = client.get_entity(name)							#получение имени канала 
 username = channel.title

 if 'new_chat_photo' in updates['result'][-1]['channel_post']:			#проверка смены фото на канале
  photo = "Photo has been changed"
 else:
  photo = "Photo hasn't been changed"

 admins=str(object="")									#проверка изменения админов
 for user in client.iter_participants(channel):
  permissions = client.get_permissions(channel, user)
  if permissions.is_admin:
   admins = admins + user.username + " "
    
 # передача в splunk в структуре json-файла
 data = {"link" : name,"username" : username,"admins":admins,"photo" : photo}
 data = json.dumps(data)
 print(data)

if __name__ == '__main__':
    main()