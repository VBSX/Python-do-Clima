import requests

API_KEY = "106dc89a610c7f04f0ebbd6186596a19"
base_url = "http://api.openweathermap.org/data/2.5/weather"
#http://api.openweathermap.org/data/2.5/weather?id=524901&appid={API_KEY}&lang={pt_br}#

city = input("Coloque a cidade desejada: ")
request_url = f"{base_url}?appid={API_KEY}&q={city}&lang=pt_br"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15 , 2)

    print("Clima: ", weather)
    print("Temperatura: ", temperature, "Celsius")
else:
    print("Algo de errado não está certo!")