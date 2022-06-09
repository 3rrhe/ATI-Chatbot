from datetime import datetime


def basic_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", 'hi', 'sup', 'hola', 'que onda', 'quepex'):
        return "Hola, en que te puedo ayudar?"

    if user_message in ("who are you", 'who are you?', '?', 'quien eres?', 'eres?', 'sos?',):
        return "Soy TheChanclasStore Bot, te ayudare a comprar las chanclas que necesites"

    if user_message in ("time", 'time?', 'hora', 'que hora es?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return 'La hora y fecha actual es: ' + str(date_time)

    if user_message in ("necesito comprar chanclas", 'comprar chanclas', 'comprar', 'chanclas', 'compra de chanclas', 'chanclas en venta', 'Busco un par de chanclas',):
        return "Será un gusto ayudar, por favor enviame el siguiente mensaje /products para que puedas ver nuestras chanclas disponibles"

    return "El dios de la chanclas no me deja ayudarte con eso, lo siento :'/"
