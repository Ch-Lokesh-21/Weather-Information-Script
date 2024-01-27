import requests
def fahrenheit_to_celsius(f):
    return round(((f - 32) * 5) / 9,1)
def mph_to_kmph(s):
    return round(s * 1.60934,2)
try:
    with open('api_key.txt', 'r') as api_key_file:
        API_KEY = api_key_file.read().strip()
    if not API_KEY:
        raise ValueError("API Key not found in the file")
    CITY = input("Enter City Name: ")
    if not CITY:
        print("Please enter a valid city name.")
    else:
        try:
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=imperial&APPID={API_KEY}")
            if weather_data.json()['cod'] == '404':
                print("Please enter valid city")
            else:    
                weather_data.raise_for_status()
                data = weather_data.json()
                weather = data['weather'][0]['main']
                temp_celsius = fahrenheit_to_celsius(data['main']['temp'])
                wind_speed_kmph = mph_to_kmph(data['wind']['speed'])
                print(f"Weather in {CITY} is: {weather}")
                print(f"Temperature in {CITY} is: {temp_celsius} °C")
                print(f"Humidity in {CITY} is: {data['main']['humidity']}%")
                print(f"Wind speed in {CITY} is: {wind_speed_kmph} kmph")
                print(f"Pressure in {CITY} is: {data['main']['pressure']} mb")
        except requests.RequestException as req_error:
            print(f"Error during API request: {req_error}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
except FileNotFoundError:
    print("API Key file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
