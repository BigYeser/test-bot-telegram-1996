

import constants as keys
import responses as r
from telegram.ext import *

print('Bot Started...')

def start_command(update, context):
    update.message.reply_text('Type something')

def help_command(update, context):
    update.message.reply_text('I cant help you!')

def handle_message(update, context):
   print(update)
   if update.message.chat['type'] == 'supergroup':
       chat_id = update.message.from_user['id']
       print(chat_id)
       user_name = update.message.from_user['first_name']
       response = r.sample_response(update.message.text)
       if chat_id == 1134269289:
           response += '\nhello boss ' + user_name
       else:
           response += '\nkol khara ' + user_name
   else:
       response = ' nothing'

   update.message.reply_text(response)

def main():
    print(1)
    updater = Updater(keys.API_KEY, use_context=True)
    print(2)
    dp = updater.dispatcher
    print(3)
    dp.add_handler(CommandHandler("start", start_command))
    print(4)
    dp.add_handler(CommandHandler("help", help_command))
    print(5)
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    print(6)
    updater.start_polling()
    print(7)
    updater.idle()


main()
