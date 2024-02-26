import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Digite a cidade: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")


#Testando a api
response_json = weather_data.json()
print(response_json)

if weather_data.json()['cod'] == '404':
    print("Cidade não encontrada")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    wind_speed = weather_data.json()['wind']['speed']
    humidity = weather_data.json()['main']['humidity']

    print(f"O clima em {user_input} é: {weather}")
    print(f"A temperatura em {user_input} é: {temp}ºC")
    print(f"A velocidade do vento em {user_input} é: {wind_speed} km/h")
    print(f"A umidade em {user_input} é: {humidity}%")
