# 샘플 Python 스크립트입니다.
# 우분투 pip3 install python-telegram-bot
import telegram
import sys
import configparser
# 우분투 추가
import os

# info
sendtele_version = 1.0
print('sendtele 버전:', sendtele_version)
# 윈도우 
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
bot = telegram.Bot(token=my_telegram_token)

if len(sys.argv) >= 2:
    val1 = sys.argv[1]
    print('telegram_token :', my_telegram_token)
    print('chat_id :', my_chat_id)
    print('메시지 내용 :', val1)
else:
    print('메시지 내용이 없습니다.')
    print('사용법 : python3 sendtele.py "메시지 내용"')
    sys.exit()

# 메시지 전송
message = val1
bot.sendMessage(chat_id=my_chat_id, text=f"{message}")
