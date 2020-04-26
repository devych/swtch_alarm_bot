import telegram
from env.api_key import telegram_token

bot = telegram.Bot(token=telegram_token)


def sendChannelMsg(text):
    if text is not None:
        bot.sendMessage(chat_id='@swtch_alarm', text=f'{text}') #@swtch_alarm