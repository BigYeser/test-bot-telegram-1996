

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
   print(context)
   if update.message.chat['type'] == 'private':
       chat_id = update.message.from_user['id']
       user_name = update.message.from_user['first_name']
       response = r.sample_response(update.message.text)
       if chat_id == 1134269289:
           response += '\nhello boss ' + user_name
       else:
           response += '\nkol khara ' + user_name

   update.message.reply_text(response)

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_handler
    updater.start_polling()
    updater.idle()

main()