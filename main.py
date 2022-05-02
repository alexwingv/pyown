
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict ['language'] = 'ru'
owm = OWM('you api key')
mgr = owm.weather_manager()

place = input ("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius') ["temp"]

print("В городе " + place + " сейчас " + w.detailed_status )
print("Температура сейчас в районе " + str(temp))
