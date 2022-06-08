import Constants as keys
from telegram.ext import *
import Responsers as R

print("Bot iniciado perras...")


def start_command(update, context):
    update.message.reply_text("Escribe algo para que te ayude prro")


def help_command(update, context):
    update.message.reply_text("Mijo googlee, no quiere que le resuelvan todo")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

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

    updater.start_polling(60)  # 60 seconds
    updater.idle()


main()
