
# Weather Information Script

This Python script retrieves real-time weather information from an external API (such as OpenWeatherMap) and displays the current weather conditions for a specified location.

## Features

- **Real-time Weather Data**: Get up-to-date weather information including temperature, humidity, wind speed, and more.
- **Location-based**: Enter a city or location to retrieve weather details.
- **Simple and Fast**: Easy-to-use script that provides weather data in seconds.
  
## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `requests` library (can be installed via pip)
- API key from [OpenWeatherMap](https://openweathermap.org/api) or another weather service.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ch-Lokesh-21/Weather-Information-Script.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Weather-Information-Script
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Open the script and add your API key in the designated area.
3. Run the script:
   ```bash
   python code.py
   ```
4. Enter the name of the city for which you want to retrieve weather data.

## Example Output

```bash
Enter city name: London
Weather in London:
Temperature: 15°C
Humidity: 80%
Wind Speed: 10 km/h
Description: Cloudy
```

## Contributing

Feel free to fork this project and contribute to its development. To contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.
