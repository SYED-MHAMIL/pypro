import tkinter as tk
from tkinter import messagebox
import requests
api_key='009c1b8153d412f26f732d0fe3a4f721'
city= input()

def get_weather(city):
    
    url =f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response= requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        pressure =main['pressure']
        humidity =main['humidity']
        description = data['weather'][0]['description']

        result = f' Wheather in city :  {city}:\n'\
                 f' Temperatire :  {temperature}%:\n'\
                 f' Humidity :  {humidity}C\n'\
                 f' Pressure :  {pressure} hPa\n'\
                 f' Description :  {description}'
        return result
    else:
       messagebox.showwarning("error","City Not Foundy")      

               

# get_weather(city)

def show_whather():
    city =city_entry.get()
    if city:
           x=  get_weather(city)
           result_label.config(text=x)
    else:
         messagebox.showwarning("error","Please enter a city")      



app= tk.Tk()
app.title("Weather app")
app.geometry('400x300')

tk.Label(app,text="Enter City Name:",font=('Helvetica',12)).pack(pady=10)
city_entry =tk.Entry(app,width=30,font=('Helvetica',12))
city_entry.pack(pady=5)
tk.Button(app,text="GET WEATHER",command=show_whather,font=('Helvetica',12)).pack(pady=6)

result_label =tk.Label(app,text='',font=('Helvetica',12),justify='left')
result_label.pack(pady=5)

app.mainloop()