import telebot
import secret
from telebot import types
from webserver import keep_alive

token = secret.token 
bot = telebot.TeleBot(token)


def write_to_file():
    file = open("users.txt", "r")
    cur_users = int(file.read())
    cur_users += 1
    new_users = str(cur_users)
    file.close()
    file = open("users.txt", "w")
    file.write(f"{new_users}")
    file.close()


@bot.message_handler(commands=['start'])
def start_message(message):
    write_to_file()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📕 Итоговое сочинение")
    btn2 = types.KeyboardButton("📃 Документы")
    btn3 = types.KeyboardButton("👋 Регистрация")
    btn4 = types.KeyboardButton("🛑 Региональные ограничения")
    btn5 = types.KeyboardButton("🏢 Пункт регистрации")
    btn6 = types.KeyboardButton("ℹ️ Основная информация")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(
        message.chat.id,
        text=
        "Привет, {0.first_name}! Я Ваш виртуальный помощник Лина. Я собрала ответы на самые популярные вопросы о регистрации на ЕГЭ для выпускников прошлых лет."
        .format(message.from_user),
        reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    # СОЧИНЕНИЕ
    if (message.text == "📕 Итоговое сочинение"):
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Основные сведения об итоговом сочинении")
        btn2 = types.KeyboardButton(
            "Где  зарегистрироваться выпускнику прошлых лет на итоговое сочинение?"
        )
        back = types.KeyboardButton("⏪ Назад")
        markup_1.add(btn1, btn2, back)
        bot.send_message(message.chat.id,
                         text="📕 Итоговое  сочинение".format(message.from_user),
                         reply_markup=markup_1)

    if (message.text == "Основные сведения об итоговом сочинении"):
        bot.send_message(
            message.chat.id,
            text=
            '''Итоговое сочинение вправе писать по желанию лица, освоившие образовательные программы среднего общего образования в предыдущие годы и имеющие документ об образовании (11 класс)  <a href="https://www.ege.spb.ru/index.php?option=com_k2&view=item&layout=item&id=204&Itemid=372">источник</a>''',
            parse_mode='html')

    if (message.text ==
            "Где  зарегистрироваться выпускнику прошлых лет на итоговое сочинение?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            "Выпускники прошлых лет регистрируются в пункте регистрации выпускников прошлых лет"
        )

    if (message.text == "⏪ Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton("📕 Итоговое сочинение")
        btn2 = types.KeyboardButton("📃 Документы")
        btn3 = types.KeyboardButton("👋 Регистрация")
        btn4 = types.KeyboardButton("🛑 Региональные ограничения")
        btn5 = types.KeyboardButton("🏢 Пункт регистрации")
        btn6 = types.KeyboardButton("ℹ️ Основная информация")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id,
                         text="Мы в главном меню 🏡".format(message.from_user),
                         reply_markup=markup)

    # ДОКУМЕНТЫ
    if (message.text == "📃 Документы"):
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton(
            "Какие документы потребуются  для регистрации ГИА-11  выпускнику прошлых лет?"
        )
        btn2 = types.KeyboardButton(
            "Можно ли принести копии документов для регистрации выпускника прошлых лет?"
        )
        btn3 = types.KeyboardButton(
            "Как зарегистрироваться на ГИА-11 несовершеннолетнему выпускнику прошлых лет?"
        )
        btn4 = types.KeyboardButton(
            "Если после регистрации на ГИА-11, я поменял документы?")
        btn5 = types.KeyboardButton(
            "Как зарегистрироваться участнику с ограниченными возможностями здоровья?"
        )
        back = types.KeyboardButton("⏪ Назад")
        markup_1.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id,
                         text="👋 Документы".format(message.from_user),
                         reply_markup=markup_1)
    if (message.text ==
            "Какие документы потребуются  для регистрации ГИА-11  выпускнику прошлых лет?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            '''Для регистрации на ГИА-11 выпускнику прошлых лет необходимо предоставить: 
- Оригинал документа, удостоверяющего личность,
- Оригинал документа об освоении программ среднего общего образования (один из следующих ниже документов):
1. Аттестат об освоении программ среднего общего образования,
2. Диплом о среднем профессиональном образовании,
3. Диплом о начальном профессиональном образовании с указанием освоения программ среднего общего образования.
''')

    if (message.text ==
            "Можно ли принести копии документов для регистрации выпускника прошлых лет?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            '''Для регистрации на ГИА-11 можно предоставлять копии, но только ЗАВЕРЕННЫЕ* (соответствующей печатью). 
 Копии документов заверяются: 
- ВУЗом (юридическое лицо, заверившее такую копию имеет правомерный доступ к подлиннику документа, заверяется в деканате учреждения),
- Образовательным учреждением (школой, лицеем, гимназией где был получен аттестат об образовании),
- Нотариусом
''')

    if (message.text ==
            "Как зарегистрироваться на ГИА-11 несовершеннолетнему выпускнику прошлых лет?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            "Несовершеннолетний (не достигший 18 лет) участник может зарегистрироваться на ГИА-11, только в присутствии родителя (законного представителя)"
        )

    if (message.text ==
            "Если после регистрации на ГИА-11, я поменял документы?"):
        bot.send_message(
            message.chat.id,
            text=
            "В пункте проведения экзамена в день его проведения Вам сделают коррекцию данных"
        )

    if (message.text ==
            "Как зарегистрироваться участнику с ограниченными возможностями здоровья?"
        ):
        bot.send_message(message.chat.id,
                         text='''
При подаче заявления участники с ограниченными возможностями здоровья могут выбрать форму прохождения ГИА-11(ЕГЭ или ГВЭ):
 "Для обеспечения особых условий при проведении ГИА-11, участники ГИА-11 с ограниченными возможностями здоровья и обучающиеся на дому при регистрации предоставляют заключение Центральной психолого-медико-педагогической комиссии Санкт-Петербурга (далее - ЦПМПК), а участники ГИА-11 дети-инвалиды и инвалиды - оригинал или заверенную в установленном порядке копию справки, подтверждающей факт установления инвалидности, выданной федеральным государственным учреждением медико-социальной экспертизы" (источник: https://www.ege.spb.ru/index.php?option=com_k2&view=item&layout=item&id=80&Itemid=310)  
Для более подробной информации об особых условиях сдачи <a href="https://www.ege.spb.ru/index.php?option=com_k2&view=item&layout=item&id=80&Itemid=310">ГИА-11 участников с ОВЗ</a>, переходите по ссылке.
''',
                         parse_mode='html')

    # РЕГИСТРАЦИЯ

    if (message.text == "👋 Регистрация"):
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton(
            "Когда начинается регистрация выпускников прошлых лет?")
        btn2 = types.KeyboardButton(
            "Если не успею зарегистрироваться до 1 февраля?")
        back = types.KeyboardButton("⏪ Назад")
        markup_1.add(btn1, btn2, back)
        bot.send_message(message.chat.id,
                         text="👋 Регистрация".format(message.from_user),
                         reply_markup=markup_1)

    if (message.text == "Когда начинается регистрация выпускников прошлых лет?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            '''Регистрация обычно начинается в конце октября – начале ноября. Более точную информацию вы можете узнать на сайте: https://www.ege.spb.ru/. Последний день регистрации  1 февраля'''
        )

    if (message.text == "Если не успею зарегистрироваться до 1 февраля?"):
        bot.send_message(
            message.chat.id,
            text=
            '''После 1 февраля, регистрация возможна, только при наличии уважительных причин, подтвержденных документально, не позднее, чем за 2 недели до проведения соответствующего экзамена.'''
        )

    # РЕГИОНАЛЬНЫЕ ОГРАНИЧЕНИЯ

    if (message.text == "🛑 Региональные ограничения"):
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton(
            "Если я зарегистрировался на ЕГЭ в другом регионе (городе), могу ли я сдавать экзамен в Санкт-Петербурге?"
        )
        btn2 = types.KeyboardButton(
            "Я могу подать документы только в том районе где проживаю?")
        back = types.KeyboardButton("⏪ Назад")
        markup_1.add(btn1, btn2, back)
        bot.send_message(message.chat.id,
                         text="🛑 Региональные ограничения".format(
                             message.from_user),
                         reply_markup=markup_1)

    if (message.text ==
            "Если я зарегистрировался на ЕГЭ в другом регионе (городе), могу ли я сдавать экзамен в Санкт-Петербурге?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            '''Да, для этого Вам нужно подать  в пункт регистрации заявление  в государственную экзаменационную комиссию (далее ГЭК). Более подровно о данной процедуре, Вы можете узнать по телефону: 417-35-34'''
        )

    if (message.text ==
            "Я могу подать документы только в том районе где проживаю?"):
        bot.send_message(
            message.chat.id,
            text=
            '''Вы можете подать документы в пунктах регистрации любого района Санкт-Петербурга'''
        )

    # ПУНКТ РЕГИСТРАЦИИ

    if (message.text == "🏢 Пункт регистрации"):
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton(
            "Часы работы пункта регистрации Калининского района?")
        btn2 = types.KeyboardButton(
            "Адрес пункта регистрации ВПЛ Калиниского района")
        btn3 = types.KeyboardButton("Есть ли он-лайн регистрация?")
        btn4 = types.KeyboardButton(
            "Статистика принятых заявлений в Пункте регистрации Калининского района"
        )
        back = types.KeyboardButton("⏪ Назад")
        markup_1.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id,
                         text="🏢 Пункт регистрации".format(message.from_user),
                         reply_markup=markup_1)

    if (message.text == "Часы работы пункта регистрации Калининского района?"):
        bot.send_message(message.chat.id,
                         text='''
Режим работы пункта регистрации:
понедельник с 10:00 до 13:00, 
среда 14:00 до 17:00,
пятница с 10:00 до 13:00
''')

    if (message.text == "Адрес пункта регистрации ВПЛ Калиниского района"):
        bot.send_message(message.chat.id,
                         text='''
Адрес:
Санкт-Петербург, ул. Софьи Ковалевской 16/6, 4 этаж, кабинет 45. (вход со двора, железная дверь под козырьком)
Контактное лицо:
Мазур Э.А.
Коноплева О.В.
Разуваев К.М.
Телефон:  417-35-34
''')

    if (message.text == "Есть ли он-лайн регистрация?"):
        bot.send_message(
            message.chat.id,
            text='''Нет, в Санкт-Петербурге, он-лайн регистрация невозможна''')

    if (message.text ==
            "Статистика принятых заявлений в Пункте регистрации Калининского района"
        ):
        bot.send_document(message.chat.id, open(r'Приложение 2.pdf', 'rb'))

    # ОСНОВНАЯ ИНФА

    if (message.text == "ℹ️ Основная информация"):
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton(
            "Где посмотреть всю информацию о регистрации (дата сдачи экзамена, условия проведения, результаты экзамена)?"
        )
        btn2 = types.KeyboardButton("Как я узнаю, где я буду сдавать экзамен?")
        btn3 = types.KeyboardButton(
            "Можно изменить выбранные предметы для сдачи?")
        btn4 = types.KeyboardButton(
            "Сколько действительны результаты ранее сданного ЕГЭ?")
        btn5 = types.KeyboardButton("Если я не согласен с результатами ЕГЭ?")
        back = types.KeyboardButton("⏪ Назад")
        markup_1.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id,
                         text="ℹ️ Основная информация".format(
                             message.from_user),
                         reply_markup=markup_1)

    if (message.text ==
            "Где посмотреть всю информацию о регистрации (дата сдачи экзамена, условия проведения, результаты экзамена)?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            '''Всю информацию Вы можете найти на сайте  https://www.ege.spb.ru/'''
        )

    if (message.text == "Как я узнаю, где я буду сдавать экзамен?"):
        bot.send_message(message.chat.id,
                         text='''
Место проведения экзамена Вы сможете узнать из уведомления,которое выдается за 1 неделю до первого экзамена в пункте регистрации, либо в <a href="https://www.ege.spb.ru/result/index.php?mode=ege2022&wave=1">личном кабинете</a> за сутки до экзамена''',
                         parse_mode='html')

    if (message.text == "Можно изменить выбранные предметы для сдачи?"):
        bot.send_message(message.chat.id,
                         text='''
Изменить перечень экзаменов возможно до 1 февраля,  после 1 февраля это  возможно только при наличии уважительных причин, подтвержденных документально, не позднее, чем за 2 недели до проведения соответствующего экзамена. Подробную информацию можно узнать по телефону: 417-35-34
''')

    if (message.text == "Сколько действительны результаты ранее сданного ЕГЭ?"
        ):
        bot.send_message(
            message.chat.id,
            text=
            '''Результаты ЕГЭ действительны 5 лет, включая год сдачи экзаменов'''
        )

    if (message.text == "Если я не согласен с результатами ЕГЭ?"):
        bot.send_message(message.chat.id,
                         text='''
В случае несогласия с результатами ЕГЭ у вас  есть возможность подать апелляцию, более подробная информация о процедуре апелляцию вы можете найти здесь: <a href="https://www.ege.spb.ru/index.php?option=com_k2&view=item&layout=item&id=42&Itemid=238">апелляция ГИА</a>.  
''',
                         parse_mode='html')

    if (message.text == "Debug count"):
        with open("users.txt", 'r', encoding = 'utf-8') as f:
          users_count = f.read()
        bot.send_message(
            message.chat.id,
            text=
            f"У нас {users_count} уникальных нажатий на Start! (После 03.10.2022) 🤩"
        )

    if (message.text == "Credit"):
        bot.send_message(
            message.chat.id,
            text=
            "👨‍💻 Создатель: Жамков Никита Д. 03.10.2007. При учебном заведении 'Кванториум' СПБ."
        )
    


keep_alive()
bot.infinity_polling()
