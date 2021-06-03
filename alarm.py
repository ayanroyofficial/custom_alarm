import time
from playsound import playsound
import datetime

x,y,z = map(int, input("Enter date in DD/MM/YYYY format = >> ").split("/"))
if z<2021:
    print("oh! you wanna time travel ?")
else:
    alarmDate = datetime.datetime(z, y, x).strftime("%x")
    alarmHour = int(input("enter hour:"))
    alarmMinute = int(input("enter minute:"))
    alarmAm = input("am / pm:")

    if alarmAm=="pm":
        alarmHour+=12


    while True:
        if alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute and alarmDate == datetime.datetime.now().strftime("%x"):

            print("hey!wake up you lazy")
            playsound('D:\\PY PROJECTS\\beep.mp3')
            break