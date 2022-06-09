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

    update.message.reply_text("Puedes usar los siguientes comandos: /covid19 /products /help /chanclas")


# This is just for test, must be deleted at the end
def covid19_command(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if (response.status_code == 200):  # Everything went okay, we have the data
        data = response.json()
        print(data)
        update.message.reply_text(data['Global'])
    else:  # something went wrong
        update.message.reply_text("No te puedo ofrecer esa información en este momento")


def get_products_command(update, context):
    response = requests.get(keys.STORE_API_URL + '/products')
    # Everything went okay, we have the data
    if (response.status_code == 200):
        data = response.json()
        print(data)
        for product in data:
            print(product['quantity'] > 0)

            if product['quantity'] > 0:
                update.message.reply_html('<b>' + product['name'] + '</b><pre>\n</pre>Precio: Q' + str(product['priceIva']) + '<pre>\n</pre>Marca: ' + product['brand'])
                update.message.reply_photo(product['image'])
    else:  # something went wrong
        update.message.reply_text("No te puedo ofrecer esa información en este momento")
