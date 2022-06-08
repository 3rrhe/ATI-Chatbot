from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", 'hi', 'sup',):
        return "Kiubas prro, que vas'querer?"

    if user_message in ("who are you", 'who are you?', '?',):
        return "Soy el bot mas vergon que vas a conocer, VIVA EUNHA <3"

    if user_message in ("seulgi",):
        return "Esa mujer te embaraza con la mirada mi pana, belleza de mujer UwU"

    if user_message in ("eunha",):
        return "No, no, no, hermano, ella si es otro nivel, supremacia Eunha presente :3 Eunha embazame UwU"

    if user_message in ("time", 'time?',):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "No idea de que queres mijo :/"
