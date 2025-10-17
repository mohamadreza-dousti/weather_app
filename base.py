from abc import ABC, abstractmethod

class weather_app_data(ABC):
    @abstractmethod
    def get_weather(self):
        pass