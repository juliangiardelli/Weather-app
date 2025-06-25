from flask import Flask, render_template, request
import datetime as dt
import requests
import unicodedata
from dictionaries import COUNTRY_CODES, WEATHER_TRANSLATIONS

app = Flask(__name__)

# URLs de las APIs con soporte para idioma
BASE_URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather?"
BASE_URL_GEO = "http://api.openweathermap.org/geo/1.0/direct?"
API_KEY = #Ingrese aquí su Key de OpenWeatherMap API

# Variables globales inicializadas como None
temperature_kelvin = None
feels_like_kelvin = None
temperature_celcius = None
temperature_fahrenheit = None
humidity = None
description = None
sunrise = None
sunset = None
response = None
CITY = None
REGION = None
COUNTRY = None
icon = None

# Normalizar strings para ignorar tildes
def normalize_string(s):
    if not s:
        return s
    normalized = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return normalized.lower()

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celcius = kelvin - 273.15
    return round(celcius)

# Function to convert Celsius to Fahrenheit
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return round(fahrenheit)

# Converting feels like temperature
def feels_like_celcius():
    feels_like_celcius = kelvin_to_celsius(feels_like_kelvin)
    return feels_like_celcius

def feels_like_fahrenheit():
    feels_like_fahrenheit = celcius_to_fahrenheit(feels_like_celcius())
    return feels_like_fahrenheit

# Function to translate weather description
def translate_weather_description(description):
    return WEATHER_TRANSLATIONS.get(description.lower(), description)

# Function to get all weather information
def get_weather_info():
    translated_description = translate_weather_description(description)
    return {
        "city": CITY.capitalize() if CITY else "",
        "region": REGION.capitalize() if REGION else "",
        "country": COUNTRY.capitalize() if COUNTRY else "",
        "temperature_celcius": temperature_celcius,
        "temperature_fahrenheit": temperature_fahrenheit,
        "feels_like_celcius": feels_like_celcius(),
        "feels_like_fahrenheit": feels_like_fahrenheit(),
        "humidity": humidity,
        "description": translated_description.capitalize(),
        "sunrise": sunrise.strftime('%Y-%m-%d %H:%M:%S') if sunrise else None,
        "sunset": sunset.strftime('%Y-%m-%d %H:%M:%S') if sunset else None,
        "icon": icon
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    global temperature_kelvin, feels_like_kelvin, temperature_celcius, temperature_fahrenheit
    global humidity, description, sunrise, sunset, response, CITY, REGION, COUNTRY, icon

    weather_data = None
    error = None
    city_input = ""

    if request.method == 'POST':
        city_input = request.form.get('city', '').strip()
        if city_input:
            # Dividir el input en partes (ciudad, región, país)
            parts = [part.strip().lower() for part in city_input.split(',')]
            city = parts[0]
            region = parts[1] if len(parts) > 1 else None
            country = parts[2] if len(parts) > 2 else parts[1] if len(parts) == 2 else None

            # Convertir nombre de país a código si se ingresó un país
            country_code = None
            if country:
                norm_country = normalize_string(country)
                for country_name, code in COUNTRY_CODES.items():
                    if normalize_string(country_name) == norm_country:
                        country_code = code
                        break
                if not country_code:
                    error = "País no reconocido. Use un país válido (ej. Argentina, España)."
                    return render_template('index.html', weather=weather_data, error=error, city=city_input)

            # Construir la URL de la Geocoding API
            geo_url = f"{BASE_URL_GEO}q={city}"
            if country_code:
                geo_url += f",{country_code}"
            geo_url += f"&limit=5&appid={API_KEY}"

            try:
                geo_response = requests.get(geo_url)
                geo_response.raise_for_status()
                geo_data = geo_response.json()

                if not geo_data:
                    error = "Ciudad no encontrada. Intente con otra ciudad (ej. San Miguel, Buenos Aires, Argentina)."
                else:
                    # Buscar la primera coincidencia válida
                    match_found = False
                    for location in geo_data:
                        loc_city = normalize_string(location['name'])
                        loc_region = normalize_string(location.get('state', ''))
                        loc_country = normalize_string(location.get('country', ''))

                        norm_city = normalize_string(city)
                        norm_region = normalize_string(region) if region else None
                        norm_country = normalize_string(country) if country else None

                        # Verificar coincidencia para ciudad y país, región es opcional
                        country_match = not norm_country or (norm_country == loc_country)
                        region_match = not norm_region or (loc_region == norm_region)
                        if loc_city == norm_city and country_match:
                            if region and region_match:
                                CITY = location['name']
                                REGION = location.get('state', '')
                                COUNTRY = location.get('country', '')
                                lat = location['lat']
                                lon = location['lon']
                                match_found = True
                                break
                            elif not region:
                                CITY = location['name']
                                REGION = location.get('state', '')
                                COUNTRY = location.get('country', '')
                                lat = location['lat']
                                lon = location['lon']
                                match_found = True
                                break

                    if not match_found:
                        error = "No se encontró una coincidencia válida. Asegúrese de que ciudad y país sean correctos."
                    else:
                        # Consultar la Weather API
                        weather_url = f"{BASE_URL_WEATHER}lat={lat}&lon={lon}&appid={API_KEY}"
                        response = requests.get(weather_url)
                        response.raise_for_status()
                        response_json = response.json()

                        if response_json.get('cod') != 200:
                            error = f"Error de la API: {response_json.get('message', 'Desconocido')}"
                        else:
                            temperature_kelvin = response_json['main']['temp']
                            temperature_celcius = kelvin_to_celsius(temperature_kelvin)
                            temperature_fahrenheit = celcius_to_fahrenheit(temperature_celcius)
                            feels_like_kelvin = response_json['main']['feels_like']
                            humidity = response_json['main']['humidity']
                            description = response_json['weather'][0]['description']
                            icon = response_json['weather'][0]['icon']
                            sunrise = dt.datetime.fromtimestamp(response_json['sys']['sunrise'] + response_json['timezone'])
                            sunset = dt.datetime.fromtimestamp(response_json['sys']['sunset'] + response_json['timezone'])

                            weather_data = get_weather_info()

            except requests.exceptions.HTTPError as http_err:
                error = f"Error HTTP: {http_err}"
            except requests.exceptions.RequestException as req_err:
                error = f"Error en la solicitud: {req_err}"
            except KeyError as key_err:
                error = f"Error en la respuesta de la API: falta la clave {key_err}"
            except Exception as e:
                error = f"Error inesperado: {e}"
        else:
            error = "Por favor, ingrese una ciudad."

    return render_template('index.html', weather=weather_data, error=error, city=city_input)

if __name__ == '__main__':
    app.run(debug=True)