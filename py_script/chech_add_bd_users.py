from email import message
import sqlite3
from tokenize import group
# from createBot import bot
from createBot import bot,weather_token
from py_script.get_weather import get_weather
import requests
from pprint import pprint
from kayboards import kb_client
from math import ceil

async def add_to_bd_user(message):
    bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_userGeo.cursor()
    mes=message.from_user.id
    info = cur_bd.execute('SELECT user_id FROM user_info WHERE user_id = ?',(mes,)).fetchone()
    if info ==None:
        cur_bd.execute("INSERT INTO user_info VALUES(?,?,?)",(mes,None,None))
        bd_userGeo.commit()

    else:
        return None


async def add_toBase_user_geo(message):
    bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_userGeo.cursor()
    lat = message.location.latitude
    lon = message.location.longitude
    ger_loc=str(lat)+"_"+str(lon)
    cur_bd.execute("UPDATE user_info SET user_geo == ? WHERE user_id == ? ",(ger_loc,message.from_user.id))
    bd_userGeo.commit()


async def chech_userId_bd_geo(message):
    bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_userGeo.cursor()
    mes=message.from_user.id
    info = cur_bd.execute('SELECT user_geo FROM user_info WHERE user_id = ?',(mes,)).fetchone()
    print(type(info),"geo")
    print(info)
    if info[0] ==None:
        return False

    else:
        return True


async def get_geo(message):
    bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_userGeo.cursor()
    id_user = message.from_user.id
    info = cur_bd.execute('SELECT user_geo FROM user_info WHERE user_id = ?',(id_user,)).fetchone()
    return info[0]



async def update_userGeo(message):
    mes_id=message.from_user.id
    bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_userGeo.cursor()
    lat = message.location.latitude
    lon = message.location.longitude
    ger_loc=str(lat)+"_"+str(lon)
    cur_bd.execute('UPDATE user_info SET user_geo == ? WHERE user_id == ?',(ger_loc,mes_id))
    bd_userGeo.commit()


# async def add_toBase_user_les(message):
#     bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
#     cur_bd = bd_userGeo.cursor()
#     flag = await chech_userId_bd(message)
    
#     cur_bd.execute("INSERT INTO user_info VALUES(?,?)",(message.from_user.id , ger_loc))
#     bd_userGeo.commit()

async def chech_userId_bd_group(message):
    bd_userGeo = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_userGeo.cursor()
    mes=message.from_user.id
    info = cur_bd.execute('SELECT user_group FROM user_info WHERE user_id = ?',(mes,)).fetchone()
    print(type(info),"gr")
    print(info)
    if info[0] ==None:
        return False

    else:
        return True

async def add_group_bd(message):
    bd_user = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_user.cursor()
    cur_bd.execute('UPDATE user_info SET user_group == ? WHERE user_id == ?',(message.text,message.from_user.id))
    bd_user.commit()


async def get_group_from_bd(message):
    bd_user = sqlite3.connect(r'py_script/bd_users/users_geo.db')
    cur_bd = bd_user.cursor()
    mes=message.from_user.id
    info = cur_bd.execute('SELECT user_group FROM user_info WHERE user_id = ?',(mes,)).fetchone()
    print(info)
    return info[0]


async def chech_group_is_real(message):
    
    group = message.text
    try:
        baseLow= sqlite3.connect(r"py_script/bd_les/Group_les_bd_low.db")
        cur_low= baseLow.cursor()

        data_result =  cur_low.execute( "SELECT * FROM Группа_{} WHERE name <> ?".format(group),("None",)).fetchall()
        return True
    except:
        return False

