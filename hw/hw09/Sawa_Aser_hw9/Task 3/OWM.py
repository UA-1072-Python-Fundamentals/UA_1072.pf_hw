from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'


def weather_owm(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
    except:
        return "Error"
    print(w.wind())
    return (f"status={w.detailed_status},\nwind_speed=n{w.wind()['speed']},\n "
            f"humidity={w.humidity},\n temperature={w.temperature('celsius')['temp']},\n "
            f"rain={w.rain},\n heat_index={w.heat_index},\n clouds={w.clouds}")
