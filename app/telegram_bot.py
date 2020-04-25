import telegram
from env.api_key import telegram_token

bot = telegram.Bot(token=telegram_token)


def sendChannelMsg(text):
    bot.sendMessage(chat_id='@ntd_swtch_alarm', text=f'{text}') #@ntd_swtch_alarm