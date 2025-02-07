# Weather API Wrapper

## Overview
This is a FastAPI-based Weather API Wrapper that fetches real-time weather data using the OpenWeather API. The API provides information such as temperature, humidity, wind speed, and sunrise/sunset times for a given city.

## Features
- Fetches weather details for any city
- Provides temperature, min/max temperature, humidity, wind speed
- Displays weather description
- Converts sunrise and sunset time to local time
- Error handling for invalid cities and missing API keys

## Technologies Used
- FastAPI
- Requests
- Python
- OpenWeather API
- dotenv (for API key security)

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Mehtab-Sidhu/weather-api.git
   cd weather-api
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv weather_env
   source weather_env/bin/activate  # On macOS/Linux
   weather_env\Scripts\activate    # On Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Create a `.env` file and add your OpenWeather API key:**
   ```sh
   echo "OPENWEATHER_API_KEY=your_api_key_here" > .env
   ```
5. **Run the API server:**
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints
- `GET /` → Welcome message
- `GET /weather?city=CityName` → Fetches weather details for the specified city

## Example Response
```json
{
    "city": "New York",
    "temperature": 22.5,
    "temp_min": 20.0,
    "temp_max": 25.0,
    "description": "clear sky",
    "humidity": 60,
    "wind_speed": 5.5,
    "sunrise": "06:30 AM",
    "sunset": "07:45 PM"
}
```

## Contributing
1. Fork the repository.
2. Create a new branch (```git checkout -b feature-branch```).
3. Commit your changes (```git commit -m 'Add new feature'```).
4. Push to the branch (```git push origin feature-branch```).
5. Open a Pull Request.

---
Happy Coding! 🌞
