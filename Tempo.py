from cProfile import label
from distutils import command
import requests
from tkinter import *

janela = Tk()

API_KEY = "106dc89a610c7f04f0ebbd6186596a19"
base_url = "http://api.openweathermap.org/data/2.5/weather"
#http://api.openweathermap.org/data/2.5/weather?id=524901&appid={API_KEY}&lang={pt_br}#

def clima_python():
    #city = input("Coloque a cidade desejada: ")
    #city = "maringa"
    request_url = f"{base_url}?appid={API_KEY}&q={city}&lang=pt_br"
    response = requests.get(request_url)
    #celcius = - 273.15 , 2
    Linha_Entrey_city = city

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperatura = round(data["main"]["temp"] - 273.15 , 2)
        sensação_termica = round(data["main"]['feels_like'] - 273.15 , 2)
        temperatura_max = round(data["main"]['temp_max'] - 273.15 , 2)
        clim =  f'''
       
        O clima está {weather}
        Temperatura em {city} é de {temperatura} °Celsius
        Com sensação térmica de {sensação_termica}°Celsius)
        '''
        texto_clima["text"]= clim
        
    else:
        erro = "Algo de errado não está certo! Tente novamente"

janela.title("Python Clima")
#janela.geometry("300x300")


texto_orientação = Label(janela, text="Seja Bem vindo Ao Python Clima!")
texto_orientação.grid(column=0, row=0, padx=10, pady=20)


texto_cidade = Label(janela, text="Insira aqui a cidade desejada", command=clima_python)
texto_cidade.grid(column=0, row=1, padx=10, pady=20)
city=Entry(janela)
city.place(x=43, y=55)


botao = Button(janela, text="Descobrir o clima")
botao.grid(column=0, row=2, padx=10, pady=10)

texto_clima = Label(janela, text="")
texto_clima.grid(column=0, row=3, padx=10, pady=10)

erro = label(janela, text="")
erro.grid(column=0, row=4)

janela.mainloop()
