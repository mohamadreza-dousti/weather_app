from api.weather_api import OpenWeather

if __name__ == '__main__':
    weather_obj = OpenWeather('Tehran')
    print(weather_obj.get_weather())