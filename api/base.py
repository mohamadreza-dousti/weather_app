from abc import ABC, abstractmethod

class weather_app(ABC):
    @abstractmethod
    def get_weather(self):
        pass
