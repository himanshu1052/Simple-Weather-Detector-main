from django.shortcuts import render
import json
import urllib.request
from urllib.parse import quote_plus  # Import the URL encoding function

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        # URL encode the city name to handle spaces and special characters
        encoded_city = quote_plus(city)
        
        # Construct the URL with the encoded city name
        url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid=cb771e45ac79a4e8e2205c0ce66ff633'
        
        # Make the request to the OpenWeather API
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        
        # Extract relevant data from the response
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',  # You can convert this to Celsius if needed
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data})
