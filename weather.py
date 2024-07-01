from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Lima"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={os.getenv('API_KEY')}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nEnter city name: ")
    # check for empty strings
    if not bool(city.strip()):
        city = "Lima"

    weather = get_current_weather(city)
    print('\n')
    pprint(weather)
