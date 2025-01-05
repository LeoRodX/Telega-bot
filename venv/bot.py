import telebot  # Импортируем telebot
from secrets import secrets  # Словарь с токеном из файла secrets.py
from dictionary import spisok  # Импортируем словарь для Списка продуктов
from telebot import types  # для указания типов


# передаём значение переменной с кодом экземпляру бота
token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)
global stroka3
stroka3 = ""

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    #global file_name
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        #file = open("./Baza/"+file_name, "rb")
        bot.send_document(call.message.chat.id, file)
        bot.send_message(call.message.chat.id, "Справочник столиц стран мира. Введите первые символы названия страны:")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Справочник столиц стран мира. Введите первые символы названия страны:")

def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #global file_name
    global stroka3
    chec = 0
    stroka1 = message.text.lower()
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Подскажу названия столиц стран мира. Введите первые символы названия страны:")
    else:
        # проверка на кирилицу
        if match(stroka1):
            #if len(stroka1) > 3:
                #  удалим символ 'я', если символов в запросе больше трех символов
            if len(stroka1) > 3:
                if stroka1[-1] == 'я':
                    # удалим последнюю 'я' в запросе
                    stroka1 = stroka1[:-1]
            #if message.text == "/start":
            #    bot.send_message(message.from_user.id, "Справочник столиц стран мира. Введите первые символы названия страны:")
            #else:
                for i in range(len(spisok)):
                    #все в нижний регистр
                    stroka01 = spisok[i][0].lower()
                    stroka02 = spisok[i][1].lower()
                    fin_stroka = []
                    if stroka01.find(stroka1) >= 0 or stroka1.find(stroka01) >= 0 or stroka02.find(stroka1) >= 0 or stroka1.find(stroka02) >= 0:
                        chec += 1 # увеличиваем счетчик на 1
                        fin_stroka.append("Столица " + spisok[i][1] + " - город " + spisok[i][0])
                        bot.send_message(message.chat.id, '\n'.join(fin_stroka))
                if chec == 0:
                    bot.send_message(message.from_user.id, "Ничего не найдено. Попробуйте другой вариант")
            else:
                bot.send_message(message.from_user.id, "Попробуйте ввести более трех литер")
        else:
            bot.send_message(message.from_user.id, "Попробуйте использовать кирилицу")

# бесконечное выполнение кода
while True:
    try:
      bot.polling(none_stop=True, interval=0)
    except:
      continue