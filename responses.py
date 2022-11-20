from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("привет", "ку", "прив", "хай"):
        return "Привет, что вам нужно?"

    if user_message in ("ты кто?", "кто ты?", "ты кто такой", "кто ты такой", "кто ты", "ты кто"):
        return "Я Hopenest бот, хозяин сделал меня для практики"

    if user_message in ("сколько времени?", "который час?", "время", "скока времени", "сколько времени"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Я не понимаю вас..."
