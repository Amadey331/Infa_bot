
import requests
from createBot import bot
from math import ceil

from createBot import weather_token
from kayboards import kb_client


async def get_weather(geo, message,token=weather_token):
    list_geo=geo.split('_')
    r = requests.get('https://api.tomorrow.io/v4/timelines?location={},{}&fields=temperature&fields=temperatureApparent&fields=windGust&timesteps=current&units=metric&apikey={}'.format(float(list_geo[0]),float(list_geo[1]),token))
    # r = requests.get('https://api.tomorrow.io/v4/timelines?location=-73.98529171943665,40.75872069597532&fields=temperature&timesteps=1h&units=metric&apikey=MpNkhObQ9Xq9wp8QX4DxLwrypORdTZYa')
    data = r.json()
    await bot.send_message(message.from_user.id , 
    f"Температура: {ceil(data['data']['timelines'][0]['intervals'][0]['values']['temperature'])}℃🌡 (Ощушается как {ceil(data['data']['timelines'][0]['intervals'][0]['values']['temperatureApparent'])}℃ )\n"
    f"Максимальная скорость ветра: {data['data']['timelines'][0]['intervals'][0]['values']['windGust']} 💨💨💨",reply_markup=kb_client)
    # await bot.send_message(message.from_user.id,data)


