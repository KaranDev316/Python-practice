# EXERCISE ON DICTIONARY COMPREHENSION

weather = {
      "New York": "snowing",
      "Boston": "sunny",
      "los angeles": "sunny"
}

sunny_weather = {key:value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)