# EXERCISE ON DICTIONARY COMPREHENSION

weather = {
      "New York": "snowing",
      "Boston": "sunny",
      "los angeles": "sunny"
}

sunny_weather = {key:value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)

#Use of if/else in dictionary comprehension
def weather_condition_check(value):
    if value < 20:
        return "Cold"
    elif value <= 30:
        return "Warm"
    else:
        return "Hot"

weather = {
      "New York": 30,
      "Boston": 25,
      "los angeles": 14
}

weather_condition = {key: ("Cold" if value < 25 else "Hot") for (key, value) in weather.items()}
weather_condition2 = {key: weather_condition_check(value) for (key, value) in weather.items()}

print(weather_condition2)