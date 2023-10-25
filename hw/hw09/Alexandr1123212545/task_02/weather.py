from pyowm import OWM


def weather(city):
    owm = OWM('62ead591e45261a878bc2cff354c53b3')
    mgr = owm.weather_manager()
    
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]

        return f"It's {temp} degrees in {city} now."
        
    except FileNotFoundError:
        return f"City {city} not found"
