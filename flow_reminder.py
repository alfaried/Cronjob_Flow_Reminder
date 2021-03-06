import os
import datetime
from telethon import TelegramClient, sync, errors
from telethon.errors import PhoneNumberUnoccupiedError, SessionPasswordNeededError

utcTime = datetime.datetime.time(datetime.datetime.utcnow()).strftime("%H:%M:%S")

API_ID = '367454'
API_HASH = '1bf84fb9cec9b739bc9dc2a5fe97ee10'
SESSION_FILE = os.path.abspath('telegram_sessions')
PHONE_NUMBER = '6591169096'
fyp_group = ''

client = TelegramClient(os.path.join(SESSION_FILE,'admin_login.session'), API_ID, API_HASH)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(PHONE_NUMBER)
    try:
        user = client.sign_in(PHONE_NUMBER, input('Enter code: '))
    except PhoneNumberUnoccupiedError:
        user = client.sign_up(PHONE_NUMBER, input('Enter code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=getpass.getpass())

dialogs = client.get_dialogs()
fyp_group = ''

for each_dialog in dialogs:
    if 'Thunderhead Monkeys' in each_dialog.name:
        fyp_group = each_dialog

if utcTime.split(':')[0] == '01':
    client.send_message(fyp_group, 'Hi, this is an automated reminder. Please complete your flow survey. \
                        \n\nWorkflow Survey: https://smu.sg/flow')
elif utcTime.split(':')[0] == '04':
    client.send_message(fyp_group, 'This is another automated reminder, please complete your flow survey. \
                        \n\nWorkflow Survey: https://smu.sg/flow')
elif utcTime.split(':')[0] == '10':
    client.send_message(fyp_group, 'Final reminder for those who have not done so, please complete your workflow survery. Thanks!\
                        \n\nWorkflow Survey: https://smu.sg/flow')
