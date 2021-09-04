# 샘플 Python 스크립트입니다.

import telegram
import sys
import configparser

# info
sendtele_version = 1.0
print('sendtele 버전:', sendtele_version)
sendtele_path = sys.executable[:-13]
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
    print('사용법 : sendtele.exe "메시지 내용"')
    sys.exit()

# 메시지 전송
message = val1
bot.sendMessage(chat_id=my_chat_id, text=f"{message}")
