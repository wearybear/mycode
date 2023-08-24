#!/usr/bin/python3

import subprocess

print("Installing necessary Python packages using pip3...")
try:
    subprocess.check_call(['pip3', 'install', 'kivy'])
    print("Packages successfully installed.")
except subprocess.CalledProcessError:
    print("Error installing packages.")

import os
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

def install_mesa_package():
    print("Installing libegl1-mesa package...")
    try:
        subprocess.check_call(['sudo', 'apt-get', 'install', 'libegl1-mesa'])
        print("libegl1-mesa successfully installed.")
    except subprocess.CalledProcessError:
        print("Error installing libegl1-mesa.")

def install_clipboard_package():
    print("Installing clipboard package (xclip)...")
    try:
        subprocess.check_call(['sudo', 'apt-get', 'install', 'xclip'])
        print("xclip successfully installed.")
    except subprocess.CalledProcessError:
        print("Error installing xclip.")

print("Setting environment variables for Kivy...")
os.environ['KIVY_METRICS_DENSITY'] = '2'
os.environ['KIVY_TEXT'] = 'sdl2'

print("Importing Kivy...")
kivy.require('1.11.1')
Config.set('graphics', 'text', 'sdl2')

class WeatherApp(App):
    def build(self):
        print("Building the app interface...")
        self.layout = BoxLayout(orientation='vertical')
        self.city_input = TextInput(hint_text='Enter city')
        self.weather_label = Label(text='Weather will be displayed here')
        self.fetch_button = Button(text='Fetch Weather', on_press=self.fetch_weather)
        
        self.layout.add_widget(self.city_input)
        self.layout.add_widget(self.fetch_button)
        self.layout.add_widget(self.weather_label)
        
        return self.layout
    
    def fetch_weather(self, instance):
        print("Fetching weather data...")
        city = self.city_input.text
        api_key = 'Instert API Key here'
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
    print("Starting the WeatherApp...")
    WeatherApp().run()

