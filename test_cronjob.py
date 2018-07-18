import getpass
from telethon import TelegramClient, sync, errors
from telethon.errors import PhoneNumberUnoccupiedError, SessionPasswordNeededError
import datetime

API_ID = '367454'
API_HASH = '1bf84fb9cec9b739bc9dc2a5fe97ee10'
phone_number = '6591169096'
fyp_group = ''

client = TelegramClient('session_name', API_ID, API_HASH)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        user = client.sign_in(phone_number, input('Enter code: '))
    except PhoneNumberUnoccupiedError:
        user = client.sign_up(phone_number, input('Enter code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=getpass.getpass())

#client.send_message('self','Testing')
client.send_message('rizzzy','Ask Prof Raph about the template for bootstrap, specifically the instructor one')
