# Weather Detector App

A simple weather detector application developed using Python and Django.

## Project Overview

This project serves as a practice during a learning journey to develop a basic weather detector app. It allows users to search for weather information of a specific city and displays details such as temperature, pressure, and humidity.

## Project Demo
https://github.com/Farahat612/Simple-Weather-Detector/assets/67427124/2d416fe4-0a09-4e77-aa0b-ff9758445a1d


## Project Structure

The project consists of the following directories and files:

1. **weatherdetector** - The main project directory.
   - `asgi.py` - ASGI configuration for the project.
   - `settings.py` - Django settings and configurations for the project.
   - `urls.py` - URL configuration for the project.
   - `wsgi.py` - WSGI configuration for the project.

2. **weather** - The app directory for managing weather-related functionality.
   - `admin.py` - Configuration for Django admin panel.
   - `apps.py` - Configuration for the app.
   - `models.py` - No models are defined in this app.
   - `tests.py` - Unit tests for the app.
   - `urls.py` - URL configuration for the app.
   - `views.py` - Views and logic for retrieving weather information.

3. **templates** - Directory containing HTML templates for rendering the views.
   - `index.html` - Template for rendering the weather detector interface.

4. `manage.py` - Django's command-line utility for managing the project.

## Usage

To run the Weather Detector app locally, follow these steps:

1. Install the required dependencies mentioned in the `requirements.txt` file.

2. Set up the project environment and database settings in `settings.py`.

3. Apply database migrations using the command: `python manage.py migrate`

4. Run the development server using the command: `python manage.py runserver`

5. Access the weather detector application in your web browser at `http://localhost:8000`.

## Features

1. **Search for Weather**: Users can search for weather information of a specific city by entering the city name in the search field.

2. **Display Weather Details**: The app retrieves the weather details from an API and displays them on the interface. The displayed information includes the country code, coordinates, temperature, pressure, and humidity.

## Important Code Files

1. **urls.py** - This file in the `weather` app configures the URL pattern for the weather application, mapping it to the corresponding view.

2. **views.py** - The `views.py` file in the `weather` app contains the logic for handling the weather detector views. It includes the `index` view, which retrieves weather information based on user input.

3. **templates** - The `templates` directory contains the HTML template used for rendering the weather detector interface. The `index.html` template displays the search form and shows the weather details when available.

## Contributing

Contributions to this project are welcome. If you wish to contribute, please follow the guidelines mentioned in the `CONTRIBUTING.md` file.

## Known Issues or Limitations

Currently, there are no known issues or limitations with this project.

Please feel free to customize this documentation according to your requirements and add any additional sections or information you deem necessary.

If you have any further questions or need additional assistance, please let me know!


