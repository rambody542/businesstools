import telegram
from telegram.ext import Updater, MessageHandler, filters
import asyncio

async def main():
  token = "6942662234:AAEp98-_YC6Wr2IQmfzx3LLumUSrnDIEyGc"
  id = "6386866903"

  bot = telegram.Bot(token)
  await bot.send_message(chat_id=id, text="자동응답 테스트 입니다. 안녕 또는 뭐해를 입력해 보세요!!")

  updater = Updater(token=token)
  dispatcher = updater.dispatcher


  async def handler(update, context):
    user_text = update.message.text
    if user_text == "안녕":
      await context.bot.send_message(chat_id=id, text="어 그래 안녕")
    elif user_text == "뭐해":
      await context.bot.send_message(chat_id=id, text="그냥 있어")
    else:
      await context.bot.send_message(chat_id=id, text="무슨")
      
  echo_handler = MessageHandler(filters.text, handler)
  dispatcher.add_handler(echo_handler)

  updater.start_polling()
  
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())