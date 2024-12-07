import requests

api_key = '08f854d73f9567d7b371cc3cedba2f26'
city_name = input('Введите назавние города на английском: ')


weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric').json()['main']
temp = weather_data['temp']
feels_like = weather_data['feels_like']
pressure = weather_data['pressure']
humidity = weather_data['humidity']


print(f'Погода в городе {city_name.capitalize()}:')
print(f'Температура: {temp}°C')
print(f'Ощущается как: {feels_like}°C')
print(f'Давление: {pressure} мм рт. ст.')
print(f'Влажность: {humidity}%')