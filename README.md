# Weather App

Aplicación web desarrollada con **Python y Flask** que permite consultar las condiciones meteorológicas de una ciudad utilizando las API de **OpenWeatherMap**.

La búsqueda admite ciudad y, opcionalmente, región y país para precisar la ubicación.

## Características

- Consulta del clima actual por ciudad.
- Búsqueda de ubicación mediante la Geocoding API de OpenWeatherMap.
- Visualización de temperatura en grados Celsius y Fahrenheit.
- Visualización de sensación térmica y humedad.
- Información de ubicación, descripción del clima, amanecer y atardecer.
- Ícono correspondiente a las condiciones meteorológicas.
- Traducción al español de las descripciones del clima mediante un diccionario propio.
- Normalización de texto para comparar nombres sin distinguir mayúsculas ni tildes.
- Fondo dinámico que cambia según las condiciones climáticas.
- Mensajes de error ante ubicaciones no encontradas o problemas de comunicación con la API.

## Tecnologías y herramientas

- Python.
- Flask.
- Requests.
- HTML5 y CSS3.
- OpenWeatherMap Geocoding API.
- OpenWeatherMap Current Weather API.
- Google Fonts: Lato y Open Sans.

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/juliangiardelli/Weather-app.git
   cd Weather-app
   ```

2. Crear y activar un entorno virtual:

   **Windows (PowerShell)**
   ```powershell
   python -m venv venv
   .\\venv\\Scripts\\Activate.ps1
   ```

   **Linux / macOS**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtener una clave API de [OpenWeatherMap](https://openweathermap.org/api) y asignarla a la variable `API_KEY` en `app.py`. La línea debe contener una cadena válida, por ejemplo:

   ```python
   API_KEY = "TU_API_KEY"
   ```

   No publiques una clave personal en repositorios públicos.

5. Iniciar la aplicación:

   ```bash
   python app.py
   ```

6. Abrir [http://localhost:5000](http://localhost:5000) en el navegador.

## Uso

1. Ingresar el nombre de una ciudad en el campo de búsqueda.
2. Para precisar el resultado, se puede indicar también la región y el país, separados por comas.
3. Presionar **Buscar** para consultar la información meteorológica.
4. La aplicación muestra los datos disponibles o un mensaje si no encuentra una ubicación válida o se produce un error en la consulta.

## Estructura del proyecto

```
Weather-app/
├── templates/
│   └── index.html       # Interfaz de la aplicación
├── app.py               # Aplicación Flask y consultas a las API
├── dictionaries.py      # Códigos de países y traducciones meteorológicas
├── requirements.txt     # Dependencias de Python
└── README.md            # Documentación del proyecto
```
