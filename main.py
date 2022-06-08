import Constants as keys
from telegram.ext import *
import Responsers as R

print(keys.BOT_NAME, "iniciado...")


def start_command(update, context):
    if keys.ENV == 'dev':
        print("comando start ejecutado")

    update.message.reply_text("Estoy aqui para ayudarte, escribe algo para comenzar o usa el comando /help")


def help_command(update, context):
    if keys.ENV == 'dev':
        print("comando help ejecutado")

    update.message.reply_text("Por el momento no te puedo ayudar aca")


def handle_message(update, context):
    if keys.ENV == 'dev':
        print("Se ha recibido un mensaje")

    text = str(update.message.text).lower()
    response = R.basic_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    # If you want the bot to have a response time, add a number in seconds inside the parenthesis.
    updater.start_polling()
    updater.idle()


main()
