import telegram
import asyncio

async def send_message_async():
  token = "6942662234:AAEp98-_YC6Wr2IQmfzx3LLumUSrnDIEyGc"
  id = "6386866903"

  bot = telegram.Bot(token)
  await bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")
  
#비동기 함수를 호출하기 위해 이벤트 루프를 생성하고 실행합니다. 
loop = asyncio.get_event_loop()
loop.run_until_complete(send_message_async())