
from createBot import bot
from kayboards import kb_client
import sqlite3


async def send_les(group, pos, message ):
    list_days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
    try:
        if pos == "Верхняя неделя ⬆️":
            baseUp= sqlite3.connect(r"py_script/bd_les/Group_les_bd_up.db")
            cur_up= baseUp.cursor()
            data_result =  cur_up.execute( "SELECT * FROM Группа_{} WHERE name <> ?".format(group),("None",)).fetchall()
            result = ""
            days= ""
            a=1
            for row in data_result:
                
                if row[0]!=days:
                    
                    result+="\n"
                    a=1

                for cell in row:
                    if cell == "None":
                        continue
                    if cell == days:
                        result+=str(a)+")"
                        continue
                    else:
                        if cell in list_days:
                            result+=cell+':'
                            result+="\n"
                            result+=str(a)+')'
                        
                        else:
                            if cell.replace(":","",2).isdigit():
                                result+=cell[:5]+" - "
                            else:
                                result+= cell+" "
                days=row[0]     
                a+=1

                result+="\n"
            await bot.send_message(message.from_user.id,result,reply_markup= kb_client)


        elif pos == "Нижняя неделя ⬇️":
            baseLow= sqlite3.connect(r"py_script/bd_les/Group_les_bd_low.db")
            cur_low= baseLow.cursor()

            data_result =  cur_low.execute( "SELECT * FROM Группа_{} WHERE name <> ?".format(group),("None",)).fetchall()


            result = ""
            days= ""
            a=1
            for row in data_result:

                if row[0]!=days:
                                                                                                                                                      
                    result+="\n"
                    a=1

                for cell in row:
                    if cell == "None":
                        continue
                    if cell == days:
                        result+=str(a)+")"
                        continue
                    else:
                        if cell in list_days:
                            result+=cell+':'
                            result+="\n"
                            result+=str(a)+')'
                        
                        else:
                            if cell.replace(":","",2).isdigit():
                                result+=cell[:5]+" - "
                            else:
                                result+= cell+" "
                days=row[0]     
                a+=1

                result+="\n"
                 

                
            await bot.send_message(message.from_user.id,result,reply_markup= kb_client)

    except:
        print(1)
        await bot.send_message(message.from_user.id,"Введена неправильная или несуществующая группа!",reply_markup= kb_client)