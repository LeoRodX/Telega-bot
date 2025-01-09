# Telega-bot

Бот по первым буквам стран или столиц подсказывает страны и их столицы.

## Песочница
  
PyCharm:  
Создать проект pythonProjectTelegaBotCapitalsWorld  

В терминале :  
python.exe -m pip install --upgrade pip  
pip install pyTelegramBotAPI  

В проводнике:  
В .env перенести bot.py, secrets.py, dictionary.py  

В телеграме, в @BotFather:  
кнМеню  
/newbot   
Название бота - Столицы государств. Справочник  
Юзер бота - CapitalsWorld_Terre_bot  
Токен - ...  
Сохраним TOKEN  
кн/editbot  
BotPic(Иконка) - 150х150  

В PyCharm:  
Вставим токен в secret.py  
Run/run bot.py  

В телеграм:  
Найдем бота по CapitalsWorld_Terre_bot, пользуемся, следуем инструкциям.  

## На сервере

1.	Создание папки capitals-bot  
2.	Добавление файлов приложения  
3.	Создание и активация виртуальной среды py_env  
4.	Обновление PIP: $ python3 -m pip install --upgrade pip  
5.	Установка библиотек: $ pip install pyTelegramBotAPI  
6.	Старт приложения: (py_env) user@xxx:~/capitals-bot$ python3 bot.py
7.	Проверка работы бота в Телеграм

## 24/7
Настройка сервера бота    
В качестве круглосуточного сервера без абонентской платы и выделенного IP можно использовать одомашненный одноплатник Orange Pi 3B с диском NVMe

1.	Переход в папку с юнитами:  
$ cd /etc/systemd/system  
2.	Создание файла(юнита) с инструкциями для systemd:  
$ sudo nano capitals-bot.service  
3.	Запись в него этого текста:  
[Service]  
#В первой части указан путь к правильному питону, установленному в виртуальную среду  
#Во второй части(после пробела) полный путь к приложению питон  
ExecStart=/home/user/capitals-bot/py_env/bin/python3 /home/user/capitals-bot/bot.py  
#Права  
User=Пользователь  
Group=ГруппаПользователя  
#Автозапуск на случай сбоя  
Restart=always    
[Install]  
#Запуск после перезагрузки  
WantedBy=multi-user.target  
4.	Сохранение и выход из nano  
5.	Старт сервиса(проекта):  
$ systemctl start capitals-bot  
6.	Статус сервиса:  
$ systemctl status capitals-bot  
7.	Добавление сервиса в автозагрузку   
$ sudo systemctl enable capitals-bot  
Created symlink /etc/systemd/system/multi-user.target.wants/capitals-bot.service → /etc/systemd/system/capitals-bot.service.  
8.	Проверка старт после перезагрузки Sudo reboot now  
$ systemctl status capitals-bot  
9.	Проверка перезапуск после сбоя  
ps -aux | grep capitals-bot  
PID во втором столбце (после пользователя) вида 34555  
Убиваем процесc:  
$ kill 34555  
Проверка авто перезапуска процесса (PID должен измениться)  
ps -aux | grep capitals-bot  
Проверка работы бота в Телеграм  


