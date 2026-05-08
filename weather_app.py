#backend for weather app project which sends an API call to openweathermap API and retreives weather data
#for any city requested. Added personalized features including option to choose fahrenheit and celsius
#and conditional weather advisory(heat, adding new advisory features in the future..)

import requests


def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather(data, city):
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    weather = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]

    unit = input("Choose F or C: ").upper()

    if unit == "C":
        units = "metric"
        symbol = "°C"
        print(f"Temperature: {(temperature - 30) / 2}°C")
        print(f"Feels Like: {(feels_like - 30) / 2}°F")
    else:
        units = "imperial"
        symbol = "°F"
        print(f"Temperature: {temperature}°F")
        print(f"Feels Like: {feels_like}°F")

    if temperature > 90:
        print("⚠️ Heat advisory")

    print("\nWeather Report")
    print("----------------")
    print(f"City: {city}")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")


def main():
    API_KEY: str = "enter API_KEY"

    city = input("Enter city name: ")

    data = get_weather(city, API_KEY)

    if data:
        display_weather(data, city)
    else:
        print("City not found or API error.")

main()
