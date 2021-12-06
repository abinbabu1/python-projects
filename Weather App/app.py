import requests, json
from flask import Flask, render_template, jsonify, session, request
from secret import api_key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    city_name = 'Delhi'
    units = 'metric'
    symbol = 'C'
    if request.method == 'POST':
        city_name = request.form.get('city')
        radio = request.form.get('inlineRadioOptions')
        if radio == 'option2':
            units = 'imperial'
            symbol = 'F'
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={units}"
    response_raw = requests.get(url)
    response = response_raw.json()
    if response_raw.status_code == 200:
        weather = {
            "city": city_name,
            "temperature": response['main']['temp'],
            "symbol": symbol,
            "feels_like": response['main']['feels_like'],
            "temp_min": response['main']['temp_min'],
            "temp_max": response['main']['temp_max'],
            "humidity": response['main']['humidity'],
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon'],
            "country": response['sys']['country'],
            "status_code": response_raw.status_code
        }
    else:
        weather = {
            'status_code': response_raw.status_code
        }
    return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run()
