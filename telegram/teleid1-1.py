import telegram
import asyncio

async def main():
  token = '6942662234:AAEp98-_YC6Wr2IQmfzx3LLumUSrnDIEyGc' # 봇의 토큰
  bot = telegram.Bot(token=token)

  updates = await bot.getUpdates()
  for u in updates:
    print(u.message)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())