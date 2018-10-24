import telegram
import datetime
from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = '661877002:AAGwwd3zN0ZLObDAObV6FqRGCQkmphEkrus'             # @SMUCLEBot
REMINDER_TOKEN = '611195322:AAFtHWQpwJBGW9cHsSzkWo99Gu5d4UmHVFM'    # @SMUCLEReminderBot
FYP_CHAT_ID = '-1001296496624'
DA_CHAT_ID = '-284543929'
SELF_CHAT_ID = '240466360'

utcDateTime = datetime.datetime.utcnow()
utcDay = datetime.datetime.date(utcDateTime).strftime("%A")
utcTime = datetime.datetime.time(utcDateTime).strftime("%H:%M:%S")

bot = telegram.Bot(token=REMINDER_TOKEN)

if utcDay == 'Saturday':
    if utcTime.split(':')[0] == '04':
        bot.send_message(chat_id=FYP_CHAT_ID, text='Hi, please complete your flow survey.\n\nWorkflow Survey: https://smu.sg/flow')
    elif utcTime.split(':')[0] == '10':
        bot.send_message(chat_id=FYP_CHAT_ID, text='Final reminder for those who have not done so, please complete your workflow survery. Thanks!\n\nWorkflow Survey: https://smu.sg/flow')

if utcDay == 'Thursday':
    if utcTime.split(':')[0] == '05':
        bot.send_message(chat_id=FYP_CHAT_ID, text='@MartinTeo and @Slaphappy remember to clear and configure DB for UT\n\n1. Course and Faculty information has to be uploaded (admin)\n2. Student and Team info has to be uploaded (faculty)\n3. Check and make sure image permission is clear in AWS account and in test server DB\n4. Goodluck')

    if utcTime.split(':')[0] == '05' and utcTime.split(':')[1] == '30':
        bot.send_message(chat_id=FYP_CHAT_ID, text='@MartinTeo and @Slaphappy final checks on testing server. Make sure everything is Aok!')

    if utcTime.split(':')[0] == '13':
        bot.send_message(chat_id=DA_CHAT_ID, text='Remember to do DA self check quiz on Elearn. Due date is 2300 hrs tomorrow!\n\nElearn link:\nhttps://elearn.smu.edu.sg')

if utcDay == 'Friday':
    if utcTime.split(':')[0] == '13':
        bot.send_message(chat_id=DA_CHAT_ID, text='Final reminder for those who have not done so, please do your DA self check quiz on Elearn. Due date is 2300 hrs today!\n\nElearn link:\nhttps://elearn.smu.edu.sg')

if utcTime.split(':')[0] == '01':
    bot.send_message(
        chat_id=FYP_CHAT_ID,
        text='<b>Daily Reminders</b>\n\n' \
            'Please remember to update group <i>"Monkey Business HQ"</i> on the:\n\n' \
            '1) Status of your task yesterday\n' \
            '2) Task you\'re working on today\n' \
            '3) And if you require any help with any task.\n\n' \
            'Monkey Business HQ Group Link:\n' \
            'https://t.me/joinchat/DlU5uFBQ-YK_fFidHRDu5w\n\n' \
            'Please also check <i>"THUNDERHEAD App updates"</i> channel before running application to get the most up to date configurations.\n\n' \
            'THUNDERHEAD App updates Group link:\n' \
            'https://t.me/joinchat/AAAAAEShIIlBDk17NJzbrg',
        parse_mode=telegram.ParseMode.HTML
    )

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
