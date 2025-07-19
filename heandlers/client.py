
from aiogram import types,Dispatcher
from createBot import dp,bot,weather_token
from heandlers.admin import FSMAdmin

from kayboards import kb_client,kb_crypto,inline_ex,kb_select_week,kb_geo,kb_replace,kb_replaceLes
from kayboards import admin_kb

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher.filters import Text

    

from py_script.translate_en_ru import translate_en_ru
from py_script.get_weather import get_weather
from py_script.get_crypt import getCryptoInfo
from py_script.create_bd import create_bdL
from py_script.show_les import send_les
from py_script.chech_add_bd_users import chech_userId_bd_geo,add_toBase_user_geo,get_geo,update_userGeo,add_to_bd_user,chech_userId_bd_group,add_group_bd,get_group_from_bd,chech_group_is_real






# Класс для состояния показа рассписания 
class FSMShowLes(StatesGroup):
    group_add_bd = State()
    what_doL = State()
    wek_pos = State()

# Класс для состояния показа погоды 
class FSMShowWeather(StatesGroup):
    what_do = State()
    user_id = State()
    
# Класс для состояния показа инфо. о крипте
class FSMShowCrypto(StatesGroup):
    coin_name = State()

class FSMgetdoc_a(StatesGroup):
    get_doc= State()


#@dp.message_handler(commands=["start","help"])
async def start_clientCommands(message:types.Message):
    # try:
    await add_to_bd_user(message)
    await bot.send_message(message.from_user.id,"Комманды:", reply_markup=kb_client)
    await message.delete()
    # except:
    #     await message.reply("Общение с ботом не возможно, для начала отправте ему личное сообщение(ссылка-https://t.me/GoInfo331_bot)")

# .......................................................................Загрузить документ............................................

# @dp.message_handler(commands=['Загрузить'])
async def get_docx(message:types.Message):   
    if message.from_user.id==896957462:
        await FSMgetdoc_a.get_doc.set()
        await bot.send_message(message.from_user.id,"Загрузите документ", reply_markup=ReplyKeyboardRemove())
        await bot.send_message(message.from_user.id,"Для отмены нажмите на кнопку",reply_markup=inline_ex)
    else:
        await bot.send_message(message.from_user.id,"Ты не админ!!!🤬🤬🤬",reply_markup=kb_client)
    

# @dp.message_handler( content_types="document",state=FSMgetdoc_a.get_doc,)
async def downloadDoc(message:types.Message,state:FSMContext):
    # try:
    
    file=await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path,r'py_script/les.xlsx')
    await create_bdL()
    await bot.send_message(message.from_user.id,'Расписание успешно загружено в базу данных!✅✅✅',reply_markup=kb_client)
    await state.finish()
        

    # except:
    #     await bot.send_message(message.from_user.id,'Ошибка с загрузкой файла')


# ........................................................................Показать расписание..............................................
#@dp.message_handler(commands=["/Показать расписание 🗓"])
async def get_group(message:types.Message):
    
    if  await chech_userId_bd_group(message):
    
        await bot.send_message(message.from_user.id,"Использовать предыдущее номер группы или добавить другой",reply_markup=kb_replaceLes)
        await FSMShowLes.what_doL.set()

    else:
        await FSMShowLes.group_add_bd.set()
        
        await bot.send_message(message.from_user.id,"Для получения информации отправьте свой номер группы",reply_markup=inline_ex)
        
        

# #@dp.message_handler(state=FSMShowLes.what_doL)
async def what_do_group(message:types.Message,state : FSMContext):
    if message.text in ('Показать группу по предыдушему запросу',"Отправить новый номер группы"):
        if message.text =="Показать группу по предыдушему запросу":
            await FSMShowLes.wek_pos.set()        
            await bot.send_message(message.from_user.id,"Выберете какую неделю отобразить",reply_markup=kb_select_week)
        else:
            await bot.send_message(message.from_user.id,"Отправьте новые данные ")
            await FSMShowLes.group_add_bd.set()
    else:
        await bot.send_message(message.from_user.id,"Ты чё кнопки не в состоянии нажать? Твоя ошибка!!!🖕🖕🖕",reply_markup=kb_client)
        await state.finish() 




# #@dp.message_handler(state=FSMShowLes.group_ad_bd)
async def add_bd_group(message:types.Message,state:FSMContext):
    if await chech_group_is_real(message):
        await add_group_bd(message)
        await bot.send_message(message.from_user.id,"Выберете какую неделю отобразить",reply_markup=kb_select_week)
        await FSMShowLes.wek_pos.set()
    else:
        await state.finish()
        await bot.send_message(message.from_user.id,"Введена неправильная или несуществующяя группа!!!",reply_markup= kb_client)
# dp.message_heandler (state=FSMShowLes.wek_pos)
async def echo_lessen(message:types.Message,state:FSMContext):
    if message.text in ('Верхняя неделя ⬆️',"Нижняя неделя ⬇️"):
        await send_les(await get_group_from_bd(message),message.text,message,)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id,"Ты чё кнопки не в состоянии нажать? Твоя ошибка!!!🖕🖕🖕",reply_markup=kb_client)
        await state.finish() 





# .....................................................................Показать погоду..............................................
# @dp.message_heandler(commands = ['Показать_погоду🌦'])
async def get_id_forWeather(message:types.Message):

    if  await chech_userId_bd_geo(message): 
    
        await bot.send_message(message.from_user.id,"Использовать предыдущее местоположение или добавить новое",reply_markup=kb_replace)
        await FSMShowWeather.what_do.set()

    else:
        await FSMShowWeather.user_id.set()
        await bot.send_message(message.from_user.id,"Для получения информации отправьте своё местоположение",reply_markup=kb_geo)
    

# @dp.message_handler(state= FSMShowWeather.what_do)
async def rep_or_echo(message:types.Message, state:FSMContext):
    if message.text in("Показать погоду по предыдущему местоположению","Отправить новое местоположение"):

    
        try:
        
            if message.text=="Показать погоду по предыдущему местоположению":
                await get_weather(await get_geo(message),message,)
                await state.finish()
            else:
                await bot.send_message(message.from_user.id,"Отправьте новое местоположение" ,reply_markup=kb_geo)
                await FSMShowWeather.user_id.set()
        except:
            await bot.send_message(message.from_user.id,"Твоя ошибка!!!🖕🖕🖕",reply_markup=kb_client) 

    else:

        await bot.send_message(message.from_user.id,"Ты чё кнопки не в состоянии нажать? Твоя ошибка!!!🖕🖕🖕",reply_markup=kb_client)
        await state.finish()

# @dp.message_heandler(state=FSMShowWeather.user_id)
async def echo_weather(message:types.Message, state:FSMContext):
    try:
        if  await chech_userId_bd_geo(message):
            await update_userGeo(message)
            await get_weather(await get_geo(message),message)
            await state.finish()
        else:
            await add_toBase_user_geo(message)
            await get_weather(await get_geo(message),message)
            await state.finish()
    except:
        await bot.send_message(message.from_user.id,"Твоя ошибка, уебан!!!🖕🖕🖕",reply_markup=kb_client) 
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Показать инфо о крипте,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# @dp.message_handler(commands= ["Показать_информацию_по_монете"])
async def get_coinName(message:types.Message):
    await bot.send_message(message.from_user.id,"Список популярных монет (если знаете полное название можете написать желаемую монету)",reply_markup=kb_crypto)
    await FSMShowCrypto.coin_name.set()


#@dp.message_heandler(state=FSMShowCrypto.coin)
async def echo_coinInfo(message:types.Message, state=FSMContext):
    await getCryptoInfo(message.text,message)
    await state.finish()







# ...............................................................Отмена состояния........................................
# dp.message_handler(state='*',commands="отмена") # State озночаен что в каком бы состоянии программа бы не находилась всегда ловить 
# dp.message_handler(Text( equals="отмена", ignore_case=True),state='*')  # Text фильтр теста тоесть как бы не написал всегда пройдёт

async def exit_FSM(message:types.Message, state= FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,'Возврат',reply_markup=kb_client)
    
# Для олавливания калбека из выхода погоды

# @dp.callback_query_handler(lambda c: c=="❌")
async def exit_callback_weather_bt(callback_query: types.CallbackQuery, state=FSMContext):
    
    await state.finish()
    await bot.send_message(callback_query.from_user.id,'Возврат',reply_markup=kb_client)


# ....................................................................В случае ессли команды нету................................................
#dp.message_handler()
async def noCommand(message:types.Message):
    await message.answer("Такой команды нет, для ознакомления используйте /help")
    await message.delete()


    


def heandler_regClient(dp:Dispatcher):
    dp.register_message_handler(start_clientCommands,commands=["start","help"])
    dp.register_message_handler(exit_FSM, lambda message:message.text=="❌", state="*")
    dp.register_callback_query_handler( exit_callback_weather_bt , lambda c: c.data=="return",state="*")
    dp.register_message_handler(get_group,lambda message:message.text == "Показать расписание🗓", state=None) # 
    dp.register_message_handler(what_do_group,state=FSMShowLes.what_doL)
    dp.register_message_handler(add_bd_group,state=FSMShowLes.group_add_bd)
    dp.register_message_handler(echo_lessen,state=FSMShowLes.wek_pos)
    dp.register_message_handler(get_id_forWeather,lambda message: message.text == "Показать погоду🌦",state=None)
    dp.register_message_handler(rep_or_echo,state=FSMShowWeather.what_do)
    dp.register_message_handler(echo_weather,content_types="location",state = FSMShowWeather.user_id)
    dp.register_message_handler(get_coinName, lambda message : message.text == "Инфорамация о монете💎" ,state=None)
    dp.register_message_handler(echo_coinInfo,state = FSMShowCrypto.coin_name)
    dp.register_message_handler(get_docx,lambda message:message.text =="Загрузить расписание")
    dp.register_message_handler(downloadDoc,content_types="document",state=FSMgetdoc_a.get_doc)
    dp.register_message_handler(noCommand)