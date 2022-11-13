import telebot

import service

api_key = "5364562464:AAG_Yz7UWN27fhsVY0Jnop51PTOd8mRbsPY"  # https://t.me/WeatherBot1800bot
bot = telebot.TeleBot(api_key)

keyboard_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_in_game = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

keyboard_menu.add('Game', 'Stats')
keyboard_in_game.add('Check', 'Pass', 'Bet')

dummy_room_number = 0
@bot.message_handler(content_types=['text'])
def logic(mes: telebot.types.Message):
    chat = mes.chat.id
    if mes.text == 'Game':
        service.FileMethods().add_to_the_room(dummy_room_number, mes.chat.first_name, 100, mes.chat.id)
        bot.send_message(chat, f'Welcome to the room # {dummy_room_number}', reply_markup=keyboard_in_game)
        total_players = service.FileMethods().get_data_from_room(dummy_room_number).__len__()
        if total_players < 6:
            d = service.FileMethods().get_data_from_room(dummy_room_number)
            users = []
            for y in d:
                users.append(d[y][0])
            if mes.chat.id not in users:
                for x in d:
                    bot.send_message(d[x][0], f'Wait, until room will be full ({total_players}/6)')
            else:
                d = service.FileMethods().get_data_from_room(dummy_room_number)
                for x in d:
                    bot.send_message(d[x][0],"game will start soon")
    elif mes.text == '/start':
        bot.send_message(chat, f"Hello, {mes.chat.first_name}",reply_markup=keyboard_menu)


bot.infinity_polling()
