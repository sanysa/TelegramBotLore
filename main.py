import time
import threading
import os
import telebot
from telebot import types

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
bot.remove_webhook()

def create_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Узнать подробности об онлайн курсе'))
    markup.add(types.KeyboardButton('Оплатить онлайн курс'))
    markup.add(types.KeyboardButton('Информация о Каринэ'))
    markup.add(types.KeyboardButton('Связаться с помощницами'))
    markup.add(types.KeyboardButton('Подробности оффлайн тренировки'))
    markup.add(types.KeyboardButton('Личная консультация'))
    markup.add(types.KeyboardButton('Сотрудничество по рекламе'))
    markup.add(types.KeyboardButton('Политика обработки персональных данных'))
    return markup

# --- функции обработчики ---
def handle_contact(message):
    bot.send_message(message.chat.id,
                     'Свяжитесь с помощницами Каринэ по следующим номерам:\n'
                     'https://wa.me/+77009123282\n'
                     'https://wa.me/+77070702532\n',
                     reply_markup=create_markup(), disable_web_page_preview=True)

def handle_information(message):
    bot.send_message(message.chat.id,
                     'Меня зовут Каринэ.\n'
                     'Я открыла женскую фитнес-студию Lore Evolution.\n'
                     'В студии есть разные направления классов.\n'
                     'Уроки веду и я сама, и команда квалифицированных тренеров.\n'
                     'Также я веду онлайн-группы. Девочки занимаются онлайн по моей программе.\n'
                     'Стаж непрерывного тренерства более 6 лет.\n'
                     'Крупный фитнес-блог в инстаграм с более чем 70,000 подписчиков.',
                     reply_markup=create_markup(), disable_web_page_preview=True)

def handle_offline_details(message):
    bot.send_message(message.chat.id,
                     'Оффлайн группа\n'
                     'Мест свободных нет , пока нет ☺️🙏\n'
                     'По информации уточнить у помощниц.\n',
                     reply_markup=create_markup())

def handle_consultation(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=(
            'Личная консультация длится 1,5 часа. На встрече (или видеосвязь) мы обсудим ваши цели (похудение, удержание веса, набор). \n'
            'Мы с вами откорректируем ваше питание, подберем персональную продуктовую корзину и создадим примерный рацион питания по вашим вкусовым предпочтениям. '
            'Дам рекомендации по тренировкам ❤️ \n'
            'После консультации через 1 неделю сделаем созвон, обсудим и посмотрим, как питание встроилось в вашу жизнь.\n'
            'Стоимость консультации 120.000 тг.\n\n'
            'https://wa.me/+77750391741'
        ),
        disable_web_page_preview=True,
        reply_markup=create_markup()
    )

def handle_advertising(message):
    bot.send_message(message.chat.id,
                     'По рекламе, все вопросы писать на\n 👇🏻👇🏻\n'
                     'https://wa.me/+77750391741\n',
                     reply_markup=create_markup(),
                     disable_web_page_preview=True)

def expire_message(chat_id, message_id):
    time.sleep(3600)
    try:
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, '⏰ Ссылка на оплату больше не активна.')
    except Exception as e:
        print(f'Ошибка при удалении сообщения: {e}')

# --- обработчики команд ---
@bot.message_handler(commands=['start'])
def main(message):
    markup = create_markup()
    bot.send_message(message.chat.id, 'Добро пожаловать в онлайн тренировки с Каринэ! Выберите действие:', reply_markup=markup)


def handle_personaldate(message):
    file_path = os.path.join(BASE_DIR, 'Политика обработки.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, f'Файл не найден: {file_path}')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Узнать подробности об онлайн курсе':
        handle_online_course_details(message)
    elif message.text == 'Оплатить онлайн курс':
        handle_payment(message)
    elif message.text == 'Информация о Каринэ':
        handle_information(message)
    elif message.text == 'Связаться с помощницами':
        handle_contact(message)
    elif message.text == 'Подробности оффлайн тренировки':
        handle_offline_details(message)
    elif message.text == 'Личная консультация':
        handle_consultation(message)
    elif message.text == 'Сотрудничество по рекламе':
        handle_advertising(message)
    elif message.text == 'Политика обработки персональных данных':
        handle_personaldate(message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, выберите действие, используя кнопки ниже.', reply_markup=create_markup())

ONLINE_COURSE_TEXT = """Онлайн группа Каринэ:

➡️Стоимость 30 000 тенге
1 месяц / 12 тренировок, лично Каринэ будет курировать группу

➡️Запись на тренировки начнется утром 23 сентября🌺😍
Запись и оплата только в день набора🔝

➡️Оплату сможете сделать, по ссылке в телеграмм боте, или же написав на указанные номера администраторов.
▶️Старт тренировок - 28 сентября‼️( будет загружена уже первая тренировка )


Кто может заниматься в группе: новички и более опытные в спорте.
- Без противопоказаний по здоровью к физическим нагрузкам (Беременным нельзя 🚫)

Как будут проходить тренировки : ↘️️
На закрытой  странице в Instagram тренировки загружаться будут  по следующему графику  :
пн, ср, пт - загружаются в 7: 00 по Астане.
Пример : в понедельник загружается тренировка утром, и она доступна до среды. В любое удобное время вы её выполняете. В среду, тренировка удаляется и загружается новый урок, и до пятницы вы так же в любое время его выполняете( видео тренировок в личку не отправляются)

Формат тренировки:
Наши тренировки выкладываются в Instagram в виде рилса. На первом видео Каринэ объясняет упражнение, затем второе упражнение выполняется вместе с ней, смотря видео ☺️

Нужно будет сделать обязательно фото до вашей фигуры до начала тренировок . 

Выполнять тренировки 3 раза в неделю тренировки- обязательный пункт ! Так как это группа онлайн, надеемся на ваше ответственное отношение к выполнению тренировок. *В случае пропуска тренировки по Вашим личным обстоятельствам- тренировка не сохраняется и не отправляется в сообщениях*🫶🏽🙏🏽

Поддержка осуществляется в закрытой группе в WhatsApp📍

➡️Что нужно из инвентаря: коврик для занятий, резинки (желательно набор с разной нагрузкой, от легких до сильных). Их много на вайлдберис или озон . Гантели  (минимум 2 кг для новичков, не новички могут взять по 4 или 5 кг). Я посоветую, какие лучше взять.

✨По питанию: на странице будет 2х часовое видео от Каринэ(доступно только до 26 октября ), все подробно о питании , кбжу и как будем формировать наш рацион. (Конкретного меню с рецептами не будет).

Будет сформирована продуктовая корзина , для понимания из чего будет состоять ваш рацион.

Уведомляем Вас, что после загрузки видео урока по питанию возврат денежных средств будет невозможен🤫 Также просим учесть, что абонемент НЕ может быть заморожен или перенесен на следующий месяц🙏🏻, так как мы закрепляем за вами место."""


def handle_online_course_details(message):
    bot.send_message(
        message.chat.id,
        ONLINE_COURSE_TEXT,
        reply_markup=create_markup()
    )

def handle_payment(message):
    file_path = os.path.join(BASE_DIR, 'Договор оферты.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, f'Файл не найден: {file_path}')

    msg = bot.send_message(message.chat.id,
                     'Оплату производить по этой ссылке 30.000 тенге: \n'
                     '👉 [Оплатить здесь](https://pay.kaspi.kz/pay/klrytula)\n'
                     '✅Оплата означает, что вы согласны с условиями Договора оферты (просим ознакомиться).\n'

                     '‼️ОБЯЗАТЕЛЬНО ‼️\n'
                     'Не забудьте отправить чек после оплаты на любой из этих номеров, чтобы вас добавили в группу.\n'

                     '👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻\n'
                     'Ватсап номера:\n'
                     'https://wa.me/+77009123282\n'
                     'https://wa.me/+77070702532\n'
                     'Убедитесь, что вы добавились в группу ватсапе, после оплаты.\n'
                     '😌Если вы не резидент Республики Казахстан, то по реквизитам обращаться по номерам указанных выше',
                     parse_mode='Markdown', disable_web_page_preview=True)

    threading.Thread(target=expire_message, args=(message.chat.id, msg.message_id), daemon=True).start()

print("BASE_DIR:", BASE_DIR)
print("FILES:", os.listdir(BASE_DIR))

bot.infinity_polling(timeout=10, long_polling_timeout=5)
