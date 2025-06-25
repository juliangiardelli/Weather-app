# Weather App

## Descripción
Weather App es una aplicación web que permite a los usuarios consultar el clima actual de cualquier ciudad utilizando la API de OpenWeatherMap. La interfaz está diseñada con una estética moderna tipo **dark mode**, con un fondo dinámico que cambia según las condiciones climáticas (soleado, nublado, lluvia, nieve, etc.).

## Características
- **Consulta del clima**: Ingresa el nombre de una ciudad para obtener información detallada, incluyendo temperatura, sensación térmica, humedad, descripción del clima, amanecer y atardecer.
- **Fondo dinámico**: El fondo de la página cambia según las condiciones climáticas:
  - Soleado: Gradiente claro (#f5f7fa a #b3d4fc).
  - Nublado: Gradiente gris (#d3d8e8 a #8798ad).
  - Lluvia/Chubasco: Gradiente oscuro (#5b7386 a #2e4053).
  - Nieve: Gradiente frío (#e6e9ef a #b0bec5).
  - Default: Gradiente azul (#6dd5ed a #2193b0).

- **Fuentes personalizadas**:
  - Títulos (`h1`, `h2`): Lato.
  - Texto general (input, botón, párrafos): Open Sans (400, 600).
- **Íconos**: Íconos blancos para detalles del clima (ubicación, temperatura, etc.) usando un filtro CSS (`invert(100%)`).
- **Traducción personalizada**: Incluye un archivo `dictionaries.py` para traducir las descripciones del clima de la API al español, mejorando la calidad de las traducciones.

## Tecnologías utilizadas
- **HTML5**: Estructura de la página.
- **CSS3**: Estilos personalizados, incluyendo transiciones, sombras y filtros.
- **Python**: Lógica del backend para procesar solicitudes.
- **Flask**: Framework web para servir la aplicación y manejar la API de OpenWeatherMap.
- **OpenWeatherMap API**: Para obtener datos climáticos en tiempo real (requiere una clave API).

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd weather-app
   ```
3. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
4. Instala las dependencias desde `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
5. Obtén una clave API de [OpenWeatherMap](https://openweathermap.org/api) e ingresala en el archivo app.py.
6. Asegúrate de que el archivo `index.html` esté en el directorio `templates/` y que `dictionaries.py` esté en el directorio raíz del proyecto.
7. Inicia el servidor Flask:
   ```bash
   python app.py
   ```

## Uso
1. Abre la aplicación en tu navegador (por ejemplo, `http://localhost:5000`).
2. Ingresa el nombre de una ciudad en el campo de búsqueda (por ejemplo, "San Miguel, Buenos Aires").
3. Haz clic en el botón "Buscar" para obtener los datos del clima.
4. Si la ciudad no se encuentra, se mostrará un mensaje de error en rojo oscuro (#7f1d1d).
5. Los resultados incluyen:
   - Ubicación (ciudad, región, país).
   - Icono del clima (de OpenWeatherMap).
   - Temperatura (en °C y °F).
   - Sensación térmica (en °C y °F).
   - Humedad (%).
   - Descripción del clima (traducida usando `dictionaries.py`).
   - Horarios de amanecer y atardecer.

## Estructura del proyecto
```
weather-app/
├── templates/
│   └── index.html    # Plantilla HTML principal
├── app.py            # Script Flask para el backend
├── dictionaries.py   # Archivo para traducción personalizada del clima
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Este archivo
```

## Estilo visual
- **Paleta de colores**:
  - Fondos: Negro con transparencia (`rgba(0, 0, 0, 0.9)`), negro claro (`#1e293b`), gris oscuro (`#334155`).
  - Textos: Blanco puro (`#ffffff`) para títulos y párrafos, gris claro (`#d1d5db`) para detalles.
  - Bordes y efectos: Gris claro (`#d1d5db`) para contenedores y botón.
  - Error: Fondo rojo oscuro (`#7f1d1d`) con texto blanco.
- **Tipografía**:
  - Títulos: Lato.
  - Texto general: Open Sans para legibilidad.
- **Íconos**: Íconos blancos generados con `filter: invert(100%)` para detalles del clima.
- **Efectos**: Sombra suave, esquinas redondeadas, y desenfoque (`backdrop-filter`).

## Notas
- **API Key**: Configura una clave válida de OpenWeatherMap en el backend para que la aplicación funcione correctamente.
- **dictionaries.py**: Este archivo contiene la lógica para traducir las descripciones del clima de la API al español, mejorando la precisión de las traducciones.
- **Personalización**: Puedes cambiar los colores de los bordes (actualmente `#d1d5db`) por otras gamas (por ejemplo, verde `#10b981`, violeta `#8b5cf6`, naranja `#f97316`) editando el CSS en `index.html`.
- **Backend**: Este README asume que usas Flask como backend. Ajusta las instrucciones si usas otra tecnología.
