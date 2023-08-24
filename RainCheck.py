#!/usr/bin/python3

pip3 install kivy
sudo apt-get install libegl1-mesa
sudo apt-get install libxrender1

export KIVY_METRICS_DENSITY=2
export KIVY_TEXT=sdl2

import kivy
kivy.require('1.11.1')  # Replace with your Kivy version
from kivy.config import Config
Config.set('graphics', 'text', 'sdl2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class WeatherApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.city_input = TextInput(hint_text='Enter city')
        self.weather_label = Label(text='Weather will be displayed here')
        self.fetch_button = Button(text='Fetch Weather', on_press=self.fetch_weather)
        
        self.layout.add_widget(self.city_input)
        self.layout.add_widget(self.fetch_button)
        self.layout.add_widget(self.weather_label)
        
        return self.layout
    
    def fetch_weather(self, instance):
        city = self.city_input.text
        api_key = 'JyJD8ZknpuBTKp6eH90mz4NFO7doWqCl'
        base_url = f'http://dataservice.accuweather.com/currentconditions/v1/{city}?apikey={api_key}'
        
        response = requests.get(base_url)
        data = response.json()
        
        if data:
            weather_text = data[0]['WeatherText']
            temperature = data[0]['Temperature']['Metric']['Value']
            self.weather_label.text = f'Weather: {weather_text}\nTemperature: {temperature}°C'
        else:
            self.weather_label.text = 'Weather data not available.'

if __name__ == '__main__':
    WeatherApp().run()

