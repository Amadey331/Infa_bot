

import requests
from createBot import bot
from kayboards import kb_client
async def getCryptoInfo(coin_name, message):
    try:
        r=requests.get(f'https://yobit.net/api/3/ticker/{coin_name.lower()}_usdt')
        
        data = r.json()
        name_c=coin_name.upper()
        price= data[f"{coin_name.lower()}_usdt"]['low']
        value = data[f"{coin_name.lower()}_usdt"]['vol']
     
        await bot.send_message(message.from_user.id,
        f"<<<{name_c}>>>\n"
        f"Цена последней сделки: {price}\n"
        f"Объём торгов: {value}"
        ,reply_markup=kb_client
        )
        await message.delete()
    except:
        await bot.send_message(message.from_user.id,'Неизвестная ошибка!',reply_markup=kb_client)

            
# r=requests.get(f"https://yobit.net/api/3/ticker/btc_usdt-nmc_btc")
# res=r.text 
# print(res)

