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

    return "Lo siento, creo que con eso no te puedo ayudar :'/"
