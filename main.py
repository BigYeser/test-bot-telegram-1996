

import constants as keys
import responses as r
import os

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
           response += '\nhello ' + user_name

   update.message.reply_text(response)

def handle_file(update, context):
   # print(update)
    context.bot.get_file(update.message.document).download("s.txt")
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print(f)


    lines = []
    with open('s.txt') as f:
        lines = f.readlines()
    
    count = 0
    for line in lines:
        count += 1
    print(f'line {count}: {line}')
       #user_name = update.message.from_user['first_name']
    #context.bot.send_message(chat_id=863672360, text='file from ' + user_name )
    #context.bot.send_document(chat_id=863672360,document=update.message.document)

    print('succes')

def main():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print(f)
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_handler(MessageHandler(Filters.document,handle_file))
    updater.start_polling()
    updater.idle()

main()
