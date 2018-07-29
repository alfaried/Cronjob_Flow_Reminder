import telegram
import datetime
from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = '661877002:AAGwwd3zN0ZLObDAObV6FqRGCQkmphEkrus'             # @SMUCLEBot
REMINDER_TOKEN = '611195322:AAFtHWQpwJBGW9cHsSzkWo99Gu5d4UmHVFM'    # @SMUCLEReminderBot
FYP_CHAT_ID = '-1001296496624'

utcTime = datetime.datetime.time(datetime.datetime.utcnow()).strftime("%H:%M:%S")

bot = telegram.Bot(token=REMINDER_TOKEN)

if utcTime.split(':')[0] == '01':
    bot.send_message(chat_id=FYP_CHAT_ID, text='Hi, this is an automated reminder. Please complete your flow survey.\n\nWorkflow Survey: https://smu.sg/flow')
elif utcTime.split(':')[0] == '04':
    bot.send_message(chat_id=FYP_CHAT_ID, text='This is another automated reminder, please complete your flow survey.\n\nWorkflow Survey: https://smu.sg/flow')
elif utcTime.split(':')[0] == '10':
    bot.send_message(chat_id=FYP_CHAT_ID, text='Final reminder for those who have not done so, please complete your workflow survery. Thanks!\n\nWorkflow Survey: https://smu.sg/flow')

# SIDE PROJECT:
# Program bot so that it can take in requests to set reminder.
# User is able to run command '/setreminder' and bot will then automatically
# schedule a reminder for that chat. The sample code at the bottom is to show how
# a bot is able to respond to a user when they type '/start'. The bot will then
# respond with a text saying "I'm a bot, please talk to me!".
#
# --- Sample Code ---
#
# def start(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
#
# updater = Updater(token=REMINDER_TOKEN)
# dispatcher = updater.dispatcher
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)
# updater.start_polling()
#
# --- End Sample Code ---
