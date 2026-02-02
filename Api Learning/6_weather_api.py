import requests
from datetime import datetime

# ---------------- API KEY ----------------
API_KEY = "cdeb7f726d9984d51a48a50b829c1705"

try:
    # ---------------- USER INPUT ----------------
    city = input("Please provide the city name: ").strip()

    if not city:
        raise ValueError("City name cannot be empty")

    # ---------------- GEO CODING API ----------------
    ENDPOINT_GEO = (
        "http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city}&limit=1&appid={API_KEY}"
    )

    geo_response = requests.get(ENDPOINT_GEO, timeout=10)
    geo_response.raise_for_status()

    geo_data = geo_response.json()

    if not geo_data:
        raise ValueError("City not found. Please enter a valid city name.")

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # ---------------- CURRENT WEATHER API ----------------
    ENDPOINT_WEATHER = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    weather_response = requests.get(ENDPOINT_WEATHER, timeout=10)
    weather_response.raise_for_status()

    data = weather_response.json()

    # ---------------- WEATHER DETAILS ----------------
    weather = data["weather"][0]["main"]

    temp = data["main"]["temp"] - 273.15
    feels_like = data["main"]["feels_like"] - 273.15
    temp_min = data["main"]["temp_min"] - 273.15
    temp_max = data["main"]["temp_max"] - 273.15
    humidity = data["main"]["humidity"]

    # wind details
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"].get("deg", "N/A")

    # sunrise & sunset (convert UNIX time)
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p")
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p")

    # ---------------- OUTPUT ----------------
    print("\n" + "=" * 35)
    print("           Weather Report")
    print("=" * 35)
    print(f"City:              {city.title()}")
    print(f"Weather:           {weather}")
    print(f"Temperature:       {temp:.2f} °C")
    print(f"Feels Like:        {feels_like:.2f} °C")
    print(f"Max Temperature:   {temp_max:.2f} °C")
    print(f"Min Temperature:   {temp_min:.2f} °C")
    print(f"Humidity:          {humidity}%")
    print(f"Wind Speed:        {wind_speed} m/s")
    print(f"Wind Direction:    {wind_deg}°")
    print(f"Sunrise Time:      {sunrise}")
    print(f"Sunset Time:       {sunset}")
    print("=" * 35)

# ---------------- ERROR HANDLING ----------------
except requests.exceptions.Timeout:
    print("❌ Request timed out. Check your internet connection.")

except requests.exceptions.HTTPError as e:
    print("❌ HTTP error occurred:", e)

except requests.exceptions.RequestException as e:
    print("❌ Network error:", e)

except ValueError as e:
    print("❌ Input error:", e)

except Exception as e:
    print("❌ Unexpected error:", e)
