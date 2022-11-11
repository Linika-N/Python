# Создать телеграм бота для задач, решенных на семинаре:
# cкачивание видео из YouTube по ссылке(и дальнейшая его отправка пользователю)

from pytube import YouTube 
from telegram import Update
from telegram.ext import Updater, MessageHandler,Filters, ContextTypes, CommandHandler

yt = YouTube('https://youtu.be/Pgs79yOlhGI')
Youtube_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

updater = Updater(token = "")

dispatcher = updater.dispatcher

def start(update:Update, context:ContextTypes):
    context.bot.send_message(chat_id = update.effective_chat.id,text = 'Для доступа к видео введите название композиции: GET')

def show_video(update:Update,context:ContextTypes):
    global Youtube_video
    msg = update.message.text.upper()
    if msg == 'GET':
        context.bot.send_video(chat_id = update.effective_chat.id,video = open(Youtube_video, 'rb'))
        context.bot.send_message(chat_id = update.effective_chat.id,text = 'Когда бот заработал)')
    else:
        context.bot.send_message(chat_id = update.effective_chat.id,text = "Ошибка в тексте, попробуй еще раз")
    return

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text,show_video))

updater.start_polling()

updater.idle()