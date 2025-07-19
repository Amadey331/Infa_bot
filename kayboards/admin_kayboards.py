from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

import kayboards



admin_kb=ReplyKeyboardMarkup(resize_keyboard=True)

bt_download = KeyboardButton("Загрузить")
bt_cancel = KeyboardButton("Отмена")

admin_kb.row(bt_download,bt_cancel)