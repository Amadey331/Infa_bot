from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


import kayboards
# Основные кнопки
bt_infoLes = KeyboardButton (("Показать расписание🗓"))
bt_infoWethaer = KeyboardButton ("Показать погоду🌦")
bt_infoCrypto = KeyboardButton ("Инфорамация о монете💎")
bt_download_les = KeyboardButton("Загрузить расписание")
bt_fulInfo = KeyboardButton ("Показать всё🖼" )


kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.row(bt_infoLes,bt_infoWethaer,bt_infoCrypto).row(bt_download_les)

# Кнопки по монетам 

bt_CBTC = KeyboardButton("BTC")
bt_CETH = KeyboardButton("ETH")
bt_CBNB = KeyboardButton("BNB")
bt_CXRP = KeyboardButton('XRP')
bt_CSOLANA = KeyboardButton("SOL")
bt_CDOGE = KeyboardButton("DOGE")
bt_exit = KeyboardButton("❌")

kb_crypto=ReplyKeyboardMarkup(resize_keyboard=True)


kb_crypto.row(bt_CBTC,bt_CETH,bt_CBNB).row(bt_CXRP,bt_CSOLANA,bt_CDOGE,bt_exit)

# кнопки для выбора недели
bt_up_w = KeyboardButton("Верхняя неделя ⬆️")
bt_low_w = KeyboardButton("Нижняя неделя ⬇️")
bt_exit_week = KeyboardButton("❌")
kb_select_week = ReplyKeyboardMarkup(resize_keyboard=True)
kb_select_week.row(bt_up_w,bt_low_w).add(bt_exit_week)

# Кнопка для выхода с погоды

inline_ex = InlineKeyboardMarkup()
btI_exit = InlineKeyboardButton(text='❌',callback_data='return')
inline_ex.add(btI_exit)


# Кнопка для отправки метсоположения
bt_geo = KeyboardButton ("Отправить местоположение 👨🏻‍🦯", request_location=True)


kb_geo= ReplyKeyboardMarkup(resize_keyboard=True)

kb_geo.row(bt_geo,bt_exit)


# Кнопи для изменения местоположения 
bt_show_wether = KeyboardButton("Показать погоду по предыдущему местоположению")
bt_replays_geo = KeyboardButton("Отправить новое местоположение")

kb_replace= ReplyKeyboardMarkup (resize_keyboard=True)

kb_replace.row(bt_show_wether,bt_replays_geo,bt_exit)

# Кнопки для изменения номера группы 

bt_show_les = KeyboardButton("Показать группу по предыдушему запросу")
bt_replays_les = KeyboardButton("Отправить новый номер группы")
kb_replaceLes= ReplyKeyboardMarkup (resize_keyboard=True)

kb_replaceLes.row(bt_show_les,bt_replays_les).add(bt_exit)