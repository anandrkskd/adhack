from weather import Weather, Unit


flocation="jaipur"


#current weather for a perticular area
def weather_current(flocation):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(flocation)
    condition = location.condition
    print("It's "+condition.text+" today")
    print("With temp "+condition.temp+"𐤏C")


if __name__=="__main__":
    weather_current(flocation)


