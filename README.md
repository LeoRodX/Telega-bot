# Capitals-bot Telegram

Бот по первым буквам стран или столиц подсказывает страны и их столицы.

Версия 2. Добавлены эмодзи флаги после названия страны.
Версия 1.

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

## Сервер

1.	Создание папки capitals-bot  
2.	Добавление в capitals-bot файлов приложения (bot.py, secrets.py, dictionary.py)  
3.	Создание и активация виртуальной среды py_env  
4.	Обновление PIP: (py_env) user@xxx:~/capitals-bot$ python3 -m pip install --upgrade pip  
5.	Установка библиотеки: (py_env) user@xxx:~/capitals-bot$ pip install pyTelegramBotAPI  
6.	Старт приложения: (py_env) user@xxx:~/capitals-bot$ python3 bot.py
7.	Проверка работы бота в Телеграм

## 24/7

Настройка сервера бота    
В качестве круглосуточного сервера без абонентской платы и выделенного IP можно использовать одомашненный одноплатник Orange Pi 3B с диском NVMe

1.	Переход в папку с юнитами: $ cd /etc/systemd/system  
2.	Создание файла(юнита) с инструкциями для systemd: $ sudo nano capitals-bot.service  
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
5.	Старт сервиса(проекта): $ systemctl start capitals-bot  
6.	Статус сервиса: $ systemctl status capitals-bot  
7.	Добавление сервиса в автозагрузку: $ sudo systemctl enable capitals-bot  
Created symlink /etc/systemd/system/multi-user.target.wants/capitals-bot.service → /etc/systemd/system/capitals-bot.service.  
8.	Проверка старт после перезагрузки Sudo reboot now: $ systemctl status capitals-bot  
9.	Проверка перезапуск после сбоя: $ ps -aux | grep capitals-bot  
PID во втором столбце (после пользователя) вида 34555  
Убиваем процесc: $ kill 34555  
Проверка авто перезапуска процесса (PID должен измениться):  $ ps -aux | grep capitals-bot  
Проверка работы бота в Телеграм  

## Обновление файлов  

1.	Подключение
Копирование помощью PuTTY. Подключимся через PuTTY
2.	Загрузка файлов во временную папку
OPIk:
Создание папки репозиториев reps в той же папке что и Documents
Переход в нее
Создание папки приложения capitals-bot
Переход в нее
Windows:
Запуск CLI
Переход в папку 1 с файлами, 
C:\Users\User>cd c:\1
Копируем через CLI(Соединение через PuTTY тоже должно быть установлено)
c:\1>pscp bot.py user@192.168.ххх.ххх:/home/user/reps/capitals-bot
3.	Остановка сервиса
$ sudo systemctl stop capitals-bot
Проверка статуса
$ sudo systemctl start capitals-bot
4.	Создание папки ver1  (удаление папки user@orangepi3b:~/reps/capitals-bot$ rm -r v1)
$ mkdir ver1
5.	Перенос в папку Old старых файлов
$ mv dictionary.py /home/wltsprsr/reps/capitals-bot/ver1
6.	Копирование новых файлов
$ cp bot.py /home/wltsprsr/capitals-bot/
7.	Старт сервиса
$ sudo systemctl start capitals-bot


