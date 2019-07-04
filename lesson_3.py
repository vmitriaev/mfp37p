# weather forecast with tips

import pyowm

owm = pyowm.OWM('9361a6fbf9cabd94ddaa011cbcd6a894', language="ru")

place = (input("Введи город: "))

observation = owm.weather_at_place(place)
w = observation.get_weather()

print(w)
