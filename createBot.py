from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

bot= Bot(token=os.getenv("TOKEN"))

weather_token=os.getenv("TOKEN_WEATHER")

dp=Dispatcher(bot, storage=storage)