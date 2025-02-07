from fastapi import FastAPI, HTTPException
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
import pytz

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_timezone(city):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(geo_url).json()

    if response and len(response) > 0:
        lat, lon = response[0]["lat"], response[0]["lon"]
        tz_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        tz_response = requests.get(tz_url).json()
        return tz_response["timezone"]
    
    return None

def convert_to_local_time(time, city):
    timezone_offset = get_timezone(city)
    
    if timezone_offset is not None:
        local_time = datetime.utcfromtimestamp(time + timezone_offset)
        return local_time.strftime('%I:%M %p')
    
    return "Timezone not found"


# Initialize the FastAPI app
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Weather API Wrapper"}

@app.get("/weather")
def get_weather(city: str):
    """Fetch weather data for a given city"""
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key is missing")
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code!=200:
        raise HTTPException(status_code=response.status_code, detail=response.json().get("message", "Error fetching data"))
    
    data = response.json()

    # Format response
    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "sunrise": convert_to_local_time(data["sys"]["sunrise"], data["name"]),
        "sunset": convert_to_local_time(data["sys"]["sunset"], data["name"]),
    }

    return weather_info