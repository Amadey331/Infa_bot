from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import  types,Dispatcher
from aiogram.dispatcher.filters import Text
from createBot import bot,dp
from kayboards import admin_kb

ID = None

class FSMAdmin(StatesGroup):
    get_doc= State()



# @dp.register_message_handler(commands=["217234915238"] , is_chat_admin=True)
async def get_admin(message:types.Message):
    global ID
    ID = message.from_user.id
    await message.reply("Вы успещно вошли в админку",reply_markup=admin_kb)


def heandler_reg_admin(dp:Dispatcher):
    dp.register_message_handler(get_admin,commands=["217234915238"],is_chat_admin= True)
    
