import telebot
import config

from telebot import types

chat_id = 131534099
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, "Select a category", reply_markup=make_start_keyboard())
    bot.register_next_step_handler(msg, first_handler)


def make_start_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    catering = types.KeyboardButton('🍴 catering')
    taxi = types.KeyboardButton('🚖 taxi')
    entertainment = types.KeyboardButton('🎭 entertainment')
    sport = types.KeyboardButton('⚽ sport')
    banks = types.KeyboardButton('💰 banks')
    large_stores = types.KeyboardButton('🏪 large stores')
    markup.add(catering, taxi, entertainment)
    markup.add(sport, banks, large_stores)
    return markup


def catering_handler(msg):
    if msg.text == 'restaurants':
        bot.send_message(msg.chat.id, config.catering_restaurants, reply_markup=make_catering_keyboard())
        bot.register_next_step_handler(msg, catering_handler)
    elif msg.text == 'bars':
        bot.send_message(msg.chat.id, config.catering_bars, reply_markup=make_catering_keyboard())
        bot.register_next_step_handler(msg, catering_handler)
    elif msg.text == 'cafe':
        bot.send_message(msg.chat.id, config.catering_cafe1, reply_markup=make_catering_keyboard())
        bot.send_message(msg.chat.id, config.catering_cafe2, reply_markup=make_catering_keyboard())
        bot.register_next_step_handler(msg, catering_handler)
    elif msg.text == 'pizzeria':
        bot.send_message(msg.chat.id, config.catering_pizzeria, reply_markup=make_catering_keyboard())
        bot.register_next_step_handler(msg, catering_handler)
    elif msg.text == 'back':
        bot.send_message(msg.chat.id, 'Go to the menu. Press any key', reply_markup=make_start_keyboard())
        bot.register_next_step_handler(msg, start_handler)


def entertainment_handler(msg):
    if msg.text == 'cinema':
        bot.send_message(msg.chat.id, config.entertainment_cinema, reply_markup=make_entertainment_keyboard())
        bot.register_next_step_handler(msg, entertainment_handler)
    elif msg.text == 'theaters':
        bot.send_message(msg.chat.id, config.entertainment_theaters, reply_markup=make_entertainment_keyboard())
        bot.register_next_step_handler(msg, entertainment_handler)
    elif msg.text == 'night clubs':
        bot.send_message(msg.chat.id, config.entertainment_night_clubs, reply_markup=make_entertainment_keyboard())
        bot.register_next_step_handler(msg, entertainment_handler)
    else:
        bot.send_message(msg.chat.id, 'Go to the menu. Press any key', reply_markup=make_start_keyboard())
        bot.register_next_step_handler(msg, start_handler)


def sport_handler(msg):
    if msg.text == 'back':
        bot.send_message(msg.chat.id, 'Go to the menu. Press any key', reply_markup=make_start_keyboard())
        bot.register_next_step_handler(msg, start_handler)
    elif msg.text == 'sports complex':
        bot.send_message(msg.chat.id, config.sport_complex1, reply_markup=make_sport_keyboard())
        bot.send_message(msg.chat.id, config.sport_complex2, reply_markup=make_sport_keyboard())
        bot.register_next_step_handler(msg, sport_handler)
    else:
        bot.send_message(msg.chat.id, config.sport_ice_rink, reply_markup=make_sport_keyboard())
        bot.register_next_step_handler(msg, sport_handler)


def large_stores_handler(msg):
    if msg.text == 'back':
        bot.send_message(msg.chat.id, 'Go to the menu. Press any key', reply_markup=make_start_keyboard())
        bot.register_next_step_handler(msg, start_handler)
    elif msg.text == 'hypermarket':
        bot.send_message(msg.chat.id, config.large_stores_hypermarket, reply_markup=make_large_stores_keyboard())
        bot.register_next_step_handler(msg, large_stores_handler)
    else:
        bot.send_message(msg.chat.id, config.large_stores_stores, reply_markup=make_large_stores_keyboard())
        bot.register_next_step_handler(msg, large_stores_handler)


def banks_handler(msg):
    if msg.text == 'Сбербанк':
        bot.send_message(msg.chat.id, config.sber, reply_markup=make_banks1_keyboard())
        bot.register_next_step_handler(msg, banks_handler)
    elif msg.text == 'ВТБ24':
        bot.send_message(msg.chat.id, config.vtb, reply_markup=make_banks1_keyboard())
        bot.register_next_step_handler(msg, banks_handler)
    elif msg.text == 'АК Барс':
        bot.send_message(msg.chat.id, config.akbars, reply_markup=make_banks1_keyboard())
        bot.register_next_step_handler(msg, banks_handler)
    elif msg.text == 'Россельхозбанк':
        bot.send_message(msg.chat.id, config.rossel, reply_markup=make_banks1_keyboard())
        bot.register_next_step_handler(msg, banks_handler)
    elif msg.text == 'back':
        bot.send_message(msg.chat.id, 'Go to the menu. Press any key', reply_markup=make_start_keyboard())
        bot.register_next_step_handler(msg, start_handler)
    else:
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_banks2_keyboard())
        bot.register_next_step_handler(msg, banks2_handler)


def banks2_handler(msg):
    if msg.text == 'Промсвязьбанк':
        bot.send_message(msg.chat.id, config.prom, reply_markup=make_banks2_keyboard())
        bot.register_next_step_handler(msg, banks2_handler)
    elif msg.text == 'Совкомбанк':
        bot.send_message(msg.chat.id, config.sov, reply_markup=make_banks2_keyboard())
        bot.register_next_step_handler(msg, banks2_handler)
    elif msg.text == 'Росгосстрах Банк':
        bot.send_message(msg.chat.id, config.rosgos, reply_markup=make_banks2_keyboard())
        bot.register_next_step_handler(msg, banks2_handler)
    elif msg.text == '👈':
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_banks1_keyboard())
        bot.register_next_step_handler(msg, banks_handler)


def make_banks1_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    sber = types.KeyboardButton('Сбербанк')
    vtb = types.KeyboardButton('ВТБ24')
    akbars = types.KeyboardButton('АК Барс')
    rossel = types.KeyboardButton('Россельхозбанк')
    back = types.KeyboardButton('back')
    forward = types.KeyboardButton('👉')
    markup.add(sber, vtb)
    markup.add(akbars, rossel)
    markup.add(back, forward)
    return markup


def make_banks2_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    prom = types.KeyboardButton('Промсвязьбанк')
    sov = types.KeyboardButton('Совкомбанк')
    rosgos = types.KeyboardButton('Росгосстрах Банк')
    back = types.KeyboardButton('👈')
    markup.add(prom, sov)
    markup.add(rosgos, back)
    return markup


def make_catering_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    restaurants = types.KeyboardButton('restaurants')
    bars = types.KeyboardButton('bars')
    cafe = types.KeyboardButton('cafe')
    pizzeria = types.KeyboardButton('pizzeria')
    back = types.KeyboardButton('back')
    markup.add(restaurants, bars)
    markup.add(cafe, pizzeria, back)
    return markup


def make_large_stores_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    hypermarket = types.KeyboardButton('hypermarket')
    stores = types.KeyboardButton('stores')
    back = types.KeyboardButton('back')
    markup.add(hypermarket, stores)
    markup.add(back)
    return markup


def make_entertainment_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    cinema = types.KeyboardButton('cinema')
    theaters = types.KeyboardButton('theaters')
    night_clubs = types.KeyboardButton('night clubs')
    back = types.KeyboardButton('back')
    markup.add(cinema, theaters, night_clubs, back)
    return markup


def make_sport_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    sports_complex = types.KeyboardButton('sports complex')
    ice_rink = types.KeyboardButton('ice rink')
    back = types.KeyboardButton('back')
    markup.add(sports_complex, ice_rink)
    markup.add(back)
    return markup


def first_handler(msg):
    if msg.text == '🚖 taxi':
        bot.send_message(msg.chat.id, config.taxi, reply_markup=make_start_keyboard())
        bot.register_next_step_handler(msg, first_handler)
    elif msg.text == '🍴 catering':
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_catering_keyboard())
        bot.register_next_step_handler(msg, catering_handler)
    elif msg.text == '🎭 entertainment':
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_entertainment_keyboard())
        bot.register_next_step_handler(msg, entertainment_handler)
    elif msg.text == '⚽ sport':
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_sport_keyboard())
        bot.register_next_step_handler(msg, sport_handler)
    elif msg.text == '💰 banks':
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_banks1_keyboard())
        bot.register_next_step_handler(msg, banks_handler)
    elif msg.text == '🏪 large stores':
        bot.send_message(msg.chat.id, 'Select', reply_markup=make_large_stores_keyboard())
        bot.register_next_step_handler(msg, large_stores_handler)


if __name__ == '__main__':
    bot.polling(none_stop=True)
