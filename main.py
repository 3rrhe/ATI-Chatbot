import Constants as keys
import Commands as cmms
from telegram.ext import *
import Responsers as R

print(keys.BOT_NAME, "iniciado...")


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

    dp.add_handler(CommandHandler("start", cmms.start_command))
    dp.add_handler(CommandHandler("help", cmms.help_command))
    dp.add_handler(CommandHandler("covid19", cmms.covid19_command))
    dp.add_handler(CommandHandler("products", cmms.get_products_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    # If you want the bot to have a response time, add a number in seconds inside the parenthesis.
    updater.start_polling()
    updater.idle()


main()
