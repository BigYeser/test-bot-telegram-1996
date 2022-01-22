import telegram

import constants as keys
import responses as r
import os

from telegram.ext import *

print('Bot Started...')
listOfMainOptions = ['مشاهدة فيديو لتعلم الاستخدام',
                     'التحدث مع وكيل',
                     'التحدث مع الدعم',
                     'تسجيل دخول',
                     'شراء بروكسي',
                     'تفقد الرصيد',
                     'تسجيل خروج',
                     ]
sessions = {}
def start_command(update, context):
    print('hello from start')
    kb = []
    msg = "مرحبا، أدخل إحدى الخيارات التالية رجاءً"
    chat_id = update.message.chat_id
    if (not (chat_id in sessions)):
        sessions[chat_id] = {}
        sessions[chat_id]['isLogin'] = False
        sessions[chat_id]['loggingIn'] = False
        sessions[chat_id]['loggingInUsername'] = False
        sessions[chat_id]['username'] = ''
        sessions[chat_id]['password'] = ''
        sessions[chat_id]['buying'] = False
        sessions[chat_id]['selectingIsp'] = False

    if (sessions[chat_id]['isLogin'] == False):
        kb = [[telegram.KeyboardButton('مشاهدة فيديو لتعلم الاستخدام')],
              [telegram.KeyboardButton('التحدث مع وكيل')],
              [telegram.KeyboardButton('التحدث مع الدعم')],
              [telegram.KeyboardButton('تسجيل دخول')]]
    else:
        kb = [[telegram.KeyboardButton('مشاهدة فيديو لتعلم الاستخدام')],
              [telegram.KeyboardButton('التحدث مع وكيل')],
              [telegram.KeyboardButton('التحدث مع الدعم')],
              [telegram.KeyboardButton('شراء بروكسي')],
              [telegram.KeyboardButton('تفقد الرصيد')],
              [telegram.KeyboardButton('تسجيل خروج')]]



        msg = "مرحبا بك أدخل إحدى الخيارات التالية رجاءً"

    kb_markup = telegram.ReplyKeyboardMarkup(kb)

    context.bot.send_message(chat_id=update.message.chat_id,
                            text=msg,
                            reply_markup=kb_markup)


def message_handler(update, context):
    msg = update.message.text
    chat_id = update.message.chat_id
    print(msg)
    list = [['اختيار ISP محدد'],['اختيار ISP عشوائي'], ['الخروج من قامئة الشراء']]
    listOfISP = [['A'], ['B'], ['C'], ['D'], ['E'],['عشوائي'], ['الخروج من قامئة الشراء']]
    if(not (chat_id in sessions)):
        sessions[chat_id] = {}
        sessions[chat_id]['isLogin'] = False
        sessions[chat_id]['loggingIn'] = False
        sessions[chat_id]['loggingInUsername'] = False
        sessions[chat_id]['username'] = ''
        sessions[chat_id]['password'] = ''
        sessions[chat_id]['buying'] = False
        sessions[chat_id]['selectingIsp'] = False
        start_command(update, context)

    else:
        if(sessions[chat_id]['selectingIsp']):
            msg = [msg]
            if(msg in listOfISP and not(msg == listOfISP[-1])):
                update.message.reply_text("تم تسجيل طلبك بنجاح")
                sessions[chat_id]['selectingIsp'] = False
                start_command(update,context)
            elif(msg == listOfISP[-1]):
                sessions[chat_id]['selectingIsp'] = False
                start_command(update,context)
            else:
                update.message.reply_text("لقد اخترت ISP خاطئ")

        elif(sessions[chat_id]['buying']):
            msg = [msg]
            if(msg == list[0]):
                kb =[]
                for isp in listOfISP :
                    kb.append(isp)
                text = "الرجاء احتيار ال ISP الذي تريده"
                kb_markup = telegram.ReplyKeyboardMarkup(kb)
                context.bot.send_message(chat_id=update.message.chat_id,
                                         text=text,
                                         reply_markup=kb_markup)
                sessions[chat_id]['buying'] = False
                sessions[chat_id]['selectingIsp'] = True
            elif(msg == list[1]):
                update.message.reply_text("تم تسجيل طلبك بنجاح")
                sessions[chat_id]['buying'] = False
                start_command(update,context)
            elif(msg == list[-1]):
                sessions[chat_id]['buying'] = False
                start_command(update,context)
            else:
                update.message.reply_text("الرجاء اختيار إحدى الخيارات التالية")

        elif(sessions[chat_id]['loggingIn']):
            if(sessions[chat_id]['loggingInUsername']):
                sessions[chat_id]['username'] = msg
                sessions[chat_id]['loggingInUsername'] = False
                update.message.reply_text("رجاءً أدخل الرقم السري")
            else:
                sessions[chat_id]['password'] = msg
                sessions[chat_id]['loggingIn'] = False
                if(sessions[chat_id]['username'] == 'abd' and sessions[chat_id]['password'] == '123'):
                    sessions[chat_id]['isLogin'] = True
                    update.message.reply_text("تم تسجيل الدخول بنجاح")
                    start_command(update,context)
                else:
                    update.message.reply_text("اسم الحساب أو الرقم السري خاطئ، حاول مرة أخرى")
        else:
            if(not(msg in listOfMainOptions)):
                start_command(update, context)
                return

            if(msg == listOfMainOptions[0]):
                context.bot.send_message(chat_id=chat_id,
                                         text="انتظر قليلاً جارِ إرسال الفيديو التعليمي")
                context.bot.send_video(chat_id=chat_id,
                                           video=open('video.mp4', 'rb'),
                                           timeout=1000)
                context.bot.send_message(chat_id=chat_id,
                                         text="استمتع بمشاهدة الفيديو!")
            elif(msg == listOfMainOptions[1]):
                context.bot.send_message(chat_id=chat_id,
                                         text='mosab: @mosabjbara')
            elif (msg == listOfMainOptions[2]):
                context.bot.send_message(chat_id=chat_id,
                                     text='abd albary: @abdtarakji  ')
            elif(msg == listOfMainOptions[3] and not(sessions[chat_id]['isLogin'])):
                sessions[chat_id]['loggingIn'] = True
                update.message.reply_text("رجاءً أدخل اسم الحساب")
                sessions[chat_id]['loggingInUsername'] = True
            elif(msg == listOfMainOptions[4] and sessions[chat_id]['isLogin']):
                kb = []
                for item in list:
                    kb.append(item)
                text = "الرجاء احتيار نوع ال ISP"
                kb_markup = telegram.ReplyKeyboardMarkup(kb)
                context.bot.send_message(chat_id=update.message.chat_id,
                                         text=text,
                                         reply_markup=kb_markup)
                sessions[chat_id]['buying'] = True
            elif(msg == listOfMainOptions[5] and sessions[chat_id]['isLogin']):
                balance = 4
                update.message.reply_text("رصيدك الحالي هو " + str(balance) + " بروكسي لهذا اليوم")
            elif(msg == listOfMainOptions[6] and sessions[chat_id]['isLogin']):
                sessions[chat_id]['isLogin'] = False
                start_command(update,context)

            else:
                start_command(update,context)



def login(update, context):
    print('login')
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text,message_handler))

    updater.start_polling()
    updater.idle()

main()
