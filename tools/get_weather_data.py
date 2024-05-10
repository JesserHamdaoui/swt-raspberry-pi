import requests

API_KEY = "dccb8fae2eb048f6a2a142629242101"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather_data(api_key=API_KEY, location="auto:ip"):

    params = {
        'key': api_key,
        'q': location,
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        
        data = response.json()

        if data and 'current' in data and 'wind_kph' in data['current']:
            wind_speed = data['current']['wind_kph']
            wind_direction = data['current'].get('wind_degree', None)
        return {
            'wind_speed': wind_speed,
            'wind_direction': wind_direction,
        }
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
