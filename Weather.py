import requests
import time
from APIToken import API_TOKEN


class current_weather: #   нужно добавить рассчёт суточных остадков
    
    def __init__(self, temp, winddirection, falls, clouds, pressure):
        self.temp = temp
        self.winddirection = winddirection
        self.falls = falls
        self.clouds = clouds
        self.pressure = pressure
    
    def h_PA_to_MM(self):
        self.pressure //= 1.33 
        
   
        
def write_to_log (logname, lodgata): 
    # нужно переписать: создание временного файла, запись lodgata, построчное копирование старого лога, сохранение временного ф-ла
    # удаление старого лога, переименоване временного ф-ла в лог-файл. Разберись, что блокирует удаление старого лога
    
    with open(logname, 'r', encoding='UTF-8') as file:
        a=file.readlines()
        a.insert(0, lodgata)
        
    with open(logname, 'w', encoding='UTF-8') as file:
        file.writelines(a)
    

time_stamp = time.strftime ("%d")+"-"+ time.strftime ("%m")+"-"+time.strftime ("%Y")+" "+ time.strftime ("%X")+ "  "
params={"q":"khimki","appid":API_TOKEN, "units":"metric", "lang":"ru" }
lineweather=""
responce = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
# Обернуть responce в TRY на случай если интернета нет



if responce:
    print("request processed OK!")
    weather = responce.json() 
    lineweather = (time_stamp + "Погода " + str(weather['name']) + ": " +  str(weather['weather'][0]['description']) + ", Температура: " 
                   + str(round((weather['main']['temp']),0)) +  "C, влажность: " + str(weather['main']['humidity']) 
                   + "%, давление: " +  str(weather['main']['pressure']) + "hPa \n")
    # переписать lineweather - разложить в объект current_weather пересчитав давление в мм ртути
    print(lineweather)
    write_to_log ('logfile.txt', lineweather)
else: 
    print('request failed')
    write_to_log ('logfile.txt', time_stamp ,  " request failed")