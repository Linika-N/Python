from telegram import Update
from telegram.ext import Updater,ContextTypes, CommandHandler 
from telegram.ext import MessageHandler,Filters
import logging
from random import randint


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO, filename="bot_log.txt")
logger = logging.getLogger(__name__)
updater = Updater(token = "5642931269:AAGoYNpUa8gBQnE3PmVCkOkbk921OOqGUhA")

dispatcher = updater.dispatcher

candies = 2021

def player_move(update: Update, context: ContextTypes):
    global candies
    context.bot.send_message(chat_id=update.effective_chat.id,text=f'''{update.effective_user.first_name}, Ваш ход.
    Сколько конфет заберем? Помни, не больше 28!    -   Осталось {candies} конфет.''')

def bot_move(update:Update, context: ContextTypes):
    if candies>=28:
        move = randint(1,28)
        update.message.reply_text(f'''Бот забирает {move} конфет/ы.''')
    else:
        move = candies
        update.message.reply_text(f'''Бот забирает {move} конфет/ы.''')
    return move

def bot_player(update:Update,context: ContextTypes):
    global candies
    # 0 индекс - это компьютер, 1 игрок - это пользователь
    players = [0,0]
    move=29
    select = randint(0,1)
    while candies!=0:
        if select == 1:
            # update.message.reply_text(f'''{update.effective_user.first_name}, Ваш ход.
            # Сколько конфет заберем? Помни, не больше 28!    -   Осталось {candies} конфет.''')
            # update.message.message_id
            player_move(update,context)
            move = int(update.message.text)
            logger.info("Move %s: %s", update.effective_user.first_name, move)
        else:
            move = bot_move(update,context)
        if candies-move>=0:
            players[select]+=move
            candies -= move
            if candies != 0:
                select = len(players)-1-select
        move=29
    if select ==0:
        update.message.reply_text("Бот выиграл!")
    else:
        update.message.reply_text(f'{update.effective_user.first_name}, выиграл/а!\nПоздравляю!!!')
def start(update: Update, context: ContextTypes):
    context.bot.send_message(chat_id=update.effective_chat.id,text = f'''Hello {update.effective_user.first_name}
    Предлагаю сыграть в игру!
    На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход.''')
    # Начнем?
    # Отправь \"Да\" для старта.)
    bot_player(update,context)

def cancel(update: Update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text("Игра окончена. Возвращайся еще!")

start_handler=CommandHandler("start", start)
player_move_handler = MessageHandler(Filters.text,player_move)
dispatcher.add_handler(start_handler)    
dispatcher.add_handler(player_move_handler)

updater.start_polling()

updater.idle()