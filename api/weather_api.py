import requests
from .base import weather_app

class OpenWeather(weather_app):
    __url = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, city_name, key="e86cd45bd2554daabe3dbe23a2c03cb5"):
        self.city_name = city_name
        self.__key = key
        self.__params = {"q" : self.city_name, "appid" : self.__key}

    def get_weather(self):
        form = requests.get(f"{OpenWeather.__url}", params=self.__params)
        form_json = form.json()
        result = {"temp" : form_json["main"]["temp"], "temp_min" : form_json["main"]["temp_min"],
                  "temp_max" : form_json["main"]["temp_max"], "sea_level" : form_json["main"]["sea_level"],
                  "city" : form_json["name"], "country" : form_json["sys"]["country"]}

        return (f"country:{result["country"]}\ncity:{result["city"]}\ntemp:{result["temp"]-273.15}\n"
                f"temp min:{result["temp_min"]-273.15}\ntemp max:{result["temp_max"]-273.15}\nsea level:{result["sea_level"]}")
