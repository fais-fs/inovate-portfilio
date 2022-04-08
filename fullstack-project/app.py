from turtle import title
from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html", mytitle = 'Fullstack')
    
@app.route("/home")
def index():
    return render_template("index.html", mytitle = 'Fullstack')

@app.route('/weather', methods = ['GET', 'POST'],)
def weather():
    if request.method == 'POST': 
        city_name = request.form['name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=e7156f4ac2b35d4e857f06f47141f65f'
        response = requests.get(url.format(city_name)).json()
        
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        icon = response['weather'][0]['icon']
        
        print(temp,weather,min_temp,max_temp,icon)
        return render_template('weather.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name)
    else:
        return render_template('weather.html')


if __name__ == "__main__":
    app.run(debug=True,port=8000)