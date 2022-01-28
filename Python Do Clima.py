from ast import Return
from cProfile import label
from distutils import command
from dotenv import load_dotenv
from PIL import Image, ImageTk
import os
import requests
from tkinter import *

load_dotenv()
janela = Tk()
base_url = "http://api.openweathermap.org/data/2.5/weather"
#http://api.openweathermap.org/data/2.5/weather?id=524901&appid={API_KEY}&lang={pt_br}#

API_KEY = os.getenv("API_KEY")
"""def salvar_dados():
    global city

    city = city.get()
"""
def clima_python():
    global city
    city = city_janela.get()
    #city = input("Coloque a cidade desejada: ")
    request_url = f"{base_url}?appid={API_KEY}&q={city}&lang=pt_br"
    response = requests.get(request_url)
    #celcius = - 273.15 , 2
    if response.status_code == 200:
        #janela_dados = Tk()
        data = response.json()
        weather = data['weather'][0]['description']
        temperatura = round(data["main"]["temp"] - 273.15 , 2)
        sensação_termica = round(data["main"]['feels_like'] - 273.15 , 2)
        temperatura_max = round(data["main"]['temp_max'] - 273.15 , 2)
        clim =  f'''
        O clima está {weather}
        Temperatura em {city} é de {temperatura}°Celsius
        Com sensação térmica de {sensação_termica}°Celsius)
        '''
        texto_clima["text"]= clim
        
    else:
        erro = f'''
        Favor Tente novamente 
        inserindo a cidade desejada
        '''
        texto_clima["text"] = erro
        #janela_dados.mainloop()
    
janela.title("Python Clima")
#janela.geometry("300x300")

img = PhotoImage(file="Imagens/Python do clima2.png")
label_imagem = Label(janela, image=img)
label_imagem.grid()

texto_orientação = Label(janela, text="Seja Bem vindo Ao Python Clima!")
texto_orientação.place(x=384)

texto_cidade = Label(janela, text="Insira aqui a cidade desejada", )
texto_cidade.place(x=390, y=50)

city_janela=Entry(janela)
city_janela.place(x=405, y=80)

botao = Button(janela, text="Descobrir o clima", command=clima_python)
botao.place(x=415, y=120)

texto_clima = Label(janela, text="")
texto_clima.place(x=350, y=300)
texto_clima.grid(pady=10)

janela.mainloop()