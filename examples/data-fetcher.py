from src.weather_data.main import OpenWeather


if __name__ == "__main__":
    weather_obj = OpenWeather("Tehran")#city_name, api_key
    result_tehran = weather_obj.get_weather()
    print(result_tehran, "\n")
    weather_obj = OpenWeather("Ardabil")#city_name, api_key
    result_ardabil = weather_obj.get_weather()
    print(result_ardabil, "\n")