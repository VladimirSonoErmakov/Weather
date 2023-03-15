import requests
import json
import time
from APIToken import API_TOKEN


class Weather: #   нужно добавить рассчёт суточных остадков
    
    def __init__(self, temp, winddirection, falls, clouds, pressure):
        self.temp = temp
        self.winddirection = winddirection
        self.falls = falls
        self.clouds = clouds
        self.pressure = pressure
    
    def h_PA_to_MM(self):
        self.pressure //= 1.33 
        
def prepare_string_for_logfile():
     pass  
        
def write_string_to_log (logname, lodgata): 
    # нужно переписать: создание временного файла, запись lodgata, построчное копирование старого лога, сохранение временного ф-ла
    # удаление старого лога, переименоване временного ф-ла в лог-файл. Разберись, что блокирует удаление старого лога
    
    with open(logname, 'r', encoding='UTF-8') as file:
        a=file.readlines()
        a.insert(0, lodgata)
        
    with open(logname, 'w', encoding='UTF-8') as file:
        file.writelines(a)
    

time_stamp = time.strftime ("%d")+"-"+ time.strftime ("%m")+"-"+time.strftime ("%Y")+" "+ time.strftime ("%X")+ "  "
params_for_API_request={"q":"khimki","appid":API_TOKEN, "units":"metric", "lang":"ru" }
weather_data_in_dictionary="" #переимунуй нормально!
API_responce = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params_for_API_request)
# Обернуть API_responce в TRY на случай если интернета нет



if API_responce:
    print("request processed OK!")
    #Weather_Data = weather_class(temp, winddirection, falls, clouds, pressure)
    #weather_data_in_dictionary=json.loads(API_responce)
   
   
   
    weather = API_responce.json() 
    weather_data_in_dictionary = (f"{time_stamp} Погода: {str(weather['name'])}: {str(weather['weather'][0]['description'])}, Температура: {str(round((weather['main']['temp']),0))}C, влажность: {str(weather['main']['humidity'])} %, давление: {str(weather['main']['pressure'])}hPa \n")
    # переписать lineweather - разложить в объект current_weather пересчитав давление в мм ртути
    print(weather_data_in_dictionary)
    #write_string_to_log ('logfile.txt', lineweather)
else: 
    print('request failed')
    write_string_to_log ('logfile.txt', time_stamp ,  " request failed")