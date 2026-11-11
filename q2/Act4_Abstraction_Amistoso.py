from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):

    def get_reading(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):

    def get_reading(self):
        return "24.5 °C"

print("---Lab Inventory System---")

print(f"[pH Sensor] Reading: {PHSensor().get_reading()}")
print(f"[Temperature Sensor] Reading: {TempSensor().get_reading()}")
print("-------------------------")

p = PHSensor()
t = TempSensor()
