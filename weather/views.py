from django.shortcuts import render, redirect

import requests

# Create your views here.

API_KEY = "9361f3813cd19596e39e9b6318ccbcbf";

def home(request):
    payLoad = {
        'message': 'not searched',
        'given_city': '',
    }
    try:
        if request.method == "GET":
            city = request.GET['city']
            payLoad['given_city'] = city
            
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

            data = requests.get(url).json()
            if(data['cod'] == '404' and data['message'] == "city not found"):
                payLoad = {
                    'message': "city not found",
                }
            else:
                payLoad = {
                    'city': data['name'],
                    'weather': data['weather'][0]['main'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'temp_kel': data['main']['temp'], #in kelvin
                    'feels_like_kel': data['main']['feels_like'], #in kelvin
                    'temp_max_kel': data['main']['temp_max'], #in kelvin
                    'temp_min_kel': data['main']['temp_min'], #in kelvin
                    'humidity': data['main']['humidity'], #in percentage
                    'pressure': data['main']['pressure'], #in mb
                    'wind_speed': data['wind']['speed'], #in m/s
                    'visibility': data['visibility'], #in m
                }

                #normal temp
                payLoad['temp_cel'] = round(payLoad['temp_kel'] - 272.15, 2)
                payLoad['temp_far'] = round(((payLoad['temp_cel']*9)/5)+32, 2)

                #feels like temp
                payLoad['feels_like_cel'] = round(payLoad['feels_like_kel'] - 272.15, 2)

                #min max temp
                payLoad['temp_max_cel'] = round(payLoad['temp_max_kel'] - 272.15, 2)
                payLoad['temp_min_cel'] = round(payLoad['temp_min_kel'] - 272.15, 2)

                #visibility to km
                payLoad['visibility_km'] = round(payLoad['visibility']/1000, 1)

                # print(payLoad)
    except:
        pass
    

    return render(request, 'index.html', payLoad);