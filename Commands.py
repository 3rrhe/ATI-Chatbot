import Constants as keys
import requests
import json

def start_command(update, context):
    if keys.ENV == 'dev':
        print("comando start ejecutado")

    update.message.reply_text("Estoy aqui para ayudarte, escribe algo para comenzar o usa el comando /help")


def help_command(update, context):
    if keys.ENV == 'dev':
        print("comando help ejecutado")

    update.message.reply_text("Por el momento no te puedo ayudar aca")

def covid19_command(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['Global'])
    else: #something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")