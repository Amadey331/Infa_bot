
from email import message
from aiogram.utils import executor
from createBot import dp,bot


async def bot_start(_):
    try:
        
        print("Бот работает")

    except:
        print("Ошибка")

        
from heandlers import client
from heandlers import admin
client.heandler_regClient(dp)
admin.heandler_reg_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=bot_start)

    
