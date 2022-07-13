# pip3 install python-telegram-bot
# import telegram
import sys
import configparser
import os
import requests

# info
sendtele_version = 1.0
print('sendtele 버전:', sendtele_version)
# 윈도우 (exe)
#sendtele_path = sys.executable[:-13]
# 우분투
sendtele_path = os.path.dirname(os.path.realpath(__file__))
print('sendtele 경로:', sendtele_path)

# sendtele.ini파일에서 정보 불러오기
config = configparser.ConfigParser()
config.read(f'{sendtele_path}/sendtele.ini')
settings = config['SETTINGS']
my_telegram_token = settings["telegram_token"]
my_chat_id = settings["chat_id"]

if len(sys.argv) >= 2:
    message = sys.argv[1]
    print('chat_id :', my_chat_id)
    print('메시지 내용 :', message)
else:
    print('메시지 내용이 없습니다.')
    print('사용법 : python3 sendtele.py "메시지 내용"')
    sys.exit()

def send_msg(text):
   token = my_telegram_token
   chat_id = my_chat_id
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)

send_msg(message)
