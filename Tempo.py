import requests

API_KEY = "106dc89a610c7f04f0ebbd6186596a19"
base_url = "http://api.openweathermap.org/data/2.5/weather"
#http://api.openweathermap.org/data/2.5/weather?id=524901&appid={API_KEY}&lang={pt_br}#

city = input("Coloque a cidade desejada: ")
request_url = f"{base_url}?appid={API_KEY}&q={city}&lang=pt_br"
response = requests.get(request_url)
celcius = - 273.15 , 2
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperatura = round(data["main"]["temp"] - 273.15 , 2)
    sensação_termica = round(data["main"]['feels_like'] - 273.15 , 2)
    temperatura_max = round(data["main"]['temp_max'] - 273.15 , 2)
    
    #print(data)
    print("O clima está", weather)
    print("Temperatura em ",city,"é de", temperatura,"°Celsius",)
    print("Com sensação térmica de",sensação_termica,"°Celsius")
    #print("A temperatura máxima hoje foi de",temperatura_max,"°Celsius")
else:
    print("Algo de errado não está certo! Tente novamente")
    