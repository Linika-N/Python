# Создать игру с ботом в телеграм.
# Условие задачи: На столе лежит 2021 конфета. Играют игрок и бот, делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.


from random import randint
from telegram import Update
from telegram.ext import Updater,ContextTypes, CommandHandler,MessageHandler,Filters
import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO, filename="bot_log.txt")
logger = logging.getLogger(__name__)
updater = Updater(token = "")

dispatcher = updater.dispatcher

def start(update:Update,context:ContextTypes):
    context.bot.send_message(chat_id=update.effective_chat.id,text = f'''Привет, {update.effective_user.first_name}
    Сыграем в игру?
    На столе лежит 2021 конфета. Играют игрок и бот, делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход.''')
    context.user_data['counter']=222
    player_choice=randint(1,2)
    if player_choice==1:
        move_text(update,context,player_choice)
    else:
        move_text(update,context,player_choice)
        bot_move(update,context)

# Информационные сообщения о ходах игроков
def move_text(update:Update,context:ContextTypes,player_choice):
    candies=context.user_data.get('counter')
    if player_choice==1:
        name = f'{update.effective_user.first_name}, Ваш ход.'
    else:
        name = 'Ход бота.'
    context.bot.send_message(chat_id=update.effective_chat.id,text=f'''{name} Осталось {candies} конфет.''')

# Завершение игры
def cancel(update:Update,context:ContextTypes):
    del context.user_data["counter"]
    update.message.reply_text("Игра завершена. Чтобы начать заново, выберите команду \"Начать игру\"")

    context.user_data.clear()

# Ход игрока
def player_move(update:Update,context:ContextTypes):
    candies = context.user_data.get('counter')
    if candies == 0 or candies== None:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Чтобы начать игру, выберите команду \"Начать игру\"")
        return
    try:
        user_text=int(update.message.text)
        if 0<user_text<29:
            move=user_text
            context.bot.send_message(chat_id=update.effective_chat.id,text=f'Вы забрали {move} конфет/ы. Осталось {candies-move} конфет/ы')
        else:
            if candies<29:
                message = f'Число должно быть от 1 до {candies}!'
            else:
                message = "Число должно быть от 1 до 28!"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return
    except Exception:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Это не число.")
    candies=candies-move
    if candies ==0:
        context.bot.send_message(chat_id = update.effective_chat.id, text='Вы выиграли! Поздравляю\nЧтобы начать заново, выберите команду \"Начать игру\"')
        return
    context.user_data['counter']=candies
    bot_move(update,context)

# Ход бота
def bot_move(update:Update,context:ContextTypes):
    candies=context.user_data.get('counter')
    if candies>28:
        move = randint(1,28)
        context.bot.send_message(chat_id = update.effective_chat.id,text = f'''Бот забирает {move} конфет/ы.''')
    else:
        move = candies
        context.bot.send_message(chat_id = update.effective_chat.id,text = f'''Бот забирает {move} конфет/ы.''')
    candies = candies - move
    if candies ==0:
        context.bot.send_message(chat_id = update.effective_chat.id, text='Бот выиграл! Поздравляю\nЧтобы начать заново, выберите команду \"Начать игру\"')    
        del context.user_data['counter']
        context.user_data.clear()
        return
    context.user_data['counter']=candies
    move_text(update,context,1)


start_game = CommandHandler("start", start)
user_move = MessageHandler(Filters.text,player_move)
game_over = CommandHandler("cancel", cancel)

dispatcher.add_handler(start_game)
dispatcher.add_handler(game_over)
dispatcher.add_handler(user_move)

updater.start_polling()

updater.idle()