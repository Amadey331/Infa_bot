@echo off
call %~dp0venv\Scripts\activate

set TOKEN=5718119213:AAFo-HtD5d7ApBPoJIBVqfSKk3uCYuHgHlM
set TOKEN_WEATHER=MpNkhObQ9Xq9wp8QX4DxLwrypORdTZYa


cd %~dp0
python infa_bot.py

pause