import telegram
import datetime
from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = '661877002:AAGwwd3zN0ZLObDAObV6FqRGCQkmphEkrus'             # @SMUCLEBot
REMINDER_TOKEN = '611195322:AAFtHWQpwJBGW9cHsSzkWo99Gu5d4UmHVFM'    # @SMUCLEReminderBot
FYP_CHAT_ID = '-1001296496624'
DA_CHAT_ID = '-284543929'

utcDateTime = datetime.datetime.utcnow()
utcDay = datetime.datetime.date(utcDateTime).strftime("%A")
utcTime = datetime.datetime.time(utcDateTime).strftime("%H:%M:%S")

bot = telegram.Bot(token=REMINDER_TOKEN)

if utcDay == 'Saturday':
    if utcTime.split(':')[0] == '01':
        bot.send_message(chat_id=FYP_CHAT_ID, text='Hi, this is an automated reminder. Please complete your flow survey.\n\nWorkflow Survey: https://smu.sg/flow')
    elif utcTime.split(':')[0] == '04':
        bot.send_message(chat_id=FYP_CHAT_ID, text='This is another automated reminder, please complete your flow survey.\n\nWorkflow Survey: https://smu.sg/flow')
    elif utcTime.split(':')[0] == '10':
        bot.send_message(chat_id=FYP_CHAT_ID, text='Final reminder for those who have not done so, please complete your workflow survery. Thanks!\n\nWorkflow Survey: https://smu.sg/flow')

if utcDay == 'Thursday':
    if utcTime.split(':')[0] == '13':
        bot.send_message(chat_id=DA_CHAT_ID, text='Remember to do DA self check quiz. Due date is 2300 hrs tomorrow!')

if utcDay == 'Friday':
    if utcTime.split(':')[0] == '12':
        bot.send_message(chat_id=DA_CHAT_ID, text='Remember to do DA self check quiz. Due date is 2300 hrs today!')
    elif utcTime.split(':')[0] == '14':
        bot.send_message(chat_id=DA_CHAT_ID, text='Final reminder, do DA self check quiz. Due date is 2300 hrs today!')

if utcTime.split(':')[0] == '01':
    bot.send_message(chat_id=FYP_CHAT_ID, text='Please remember to update group Monkey Business HQ on the:\n\n1) Status of your task yesterday\n2) Task you\'re working on today\n3) And if you require any help with any task.\n\nThanks!')


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
