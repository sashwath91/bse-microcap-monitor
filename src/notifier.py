from telegram import Bot

def send_alerts(messages: list[str], token: str, chat_id: str):
    bot = Bot(token=token)
    for msg in messages:
        bot.send_message(chat_id=chat_id, text=msg)
