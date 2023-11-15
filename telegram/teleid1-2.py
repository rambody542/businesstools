import telegram
import asyncio

async def main():
    token = '6942662234:AAEp98-_YC6Wr2IQmfzx3LLumUSrnDIEyGc' # 봇의 토큰
    bot = telegram.Bot(token=token)
    
    # 봇이 받은 메시지 중 하나를 가져옵니다.
    updates = await bot.getUpdates()
    
    if updates:
        message = updates[0].message
        chat_id = message.chat_id
        print(f"봇 아이디(수신자): {chat_id}")
    else:
        print("봇이 받은 메시지가 없습니다.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())