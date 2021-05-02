import requests
from flask import Flask, render_template, request
#import mySQLdb.cursors

app = Flask(__name__)


weather_data = set()
invalid = True
@app.route('/', methods=['GET', 'POST'])
def index():

    invalid = False
    new_city = ""
    if request.method == 'POST':
        new_city = request.form.get('city')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ef0491ff93740084789aa0a00863f04a'
    city = new_city
    city_list = new_city.split(',')
    city_list.extend(weather_data)

    #try:
    current_weather_data= {}
    for city in city_list:
        try:
            r = requests.get(url.format(city)).json()
            weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
        except:
            #render_template('weather.html', invalid=True)
            invalid = True
            continue


        weather_data.add(city)
        current_weather_data[city] = weather
    print(r)
    return render_template('weather.html', weather_data=current_weather_data.values())
    # except KeyError:
    #     return render_template('weather.html', invalid=True)







if __name__ == '__main__':
    app.debug = True

    app.run(host='0.0.0.0')
    weather_data.clear()