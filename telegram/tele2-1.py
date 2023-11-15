import telegram
from telegram.ext import Updater, MessageHandler, filters


def send_message():
  token = "6942662234:AAEp98-_YC6Wr2IQmfzx3LLumUSrnDIEyGc" # 봇의 토큰을 넣어주세요
  id = "6386866903" # 대상 채팅의 ID를 넣어주세요


  bot = telegram.Bot(token)
  bot.send_message(chat_id=id, text="자동응답 테스트입니다. 안녕 또는 뭐해를 입력하여 보세요")


  updater = Updater(bot=bot, use_context=True)
  dp = updater.dispatcher


  def handler(update, context):
    user_text = update.message.text
    if user_text == "안녕":
      context.bot.send_message(chat_id=update.effective_chat.id, text="어 그래 안녕")
    elif user_text == "뭐해":
      context.bot.send_message(chat_id=update.effective_chat.id, text="그냥 있어")

  echo_handler = MessageHandler(filters.text & ~filters.command, handler)
  dp.add_handler(echo_handler)

  updater.start_polling()


if __name__ == "__main__":
    send_message()