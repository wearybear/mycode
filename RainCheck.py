#!/usr/bin/python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests

class WeatherApp(App):
    def build(self):
        self.title = 'RainCheck'
        self.orientation = 'vertical'
        
        self.city_input = TextInput(hint_text='Enter City, State')
        self.fetch_button = Button(text='Fetch Weather')
        self.weather_label = Label(text='', halign='center')
        
        self.fetch_button.bind(on_press=self.fetch_weather)
        
        self.add_widget(self.city_input)
        self.add_widget(self.fetch_button)
        self.add_widget(self.weather_label)
        
        return self
    
    def fetch_weather(self, instance):
        city_state = self.city_input.text
        if not city_state:
            self.weather_label.text = 'Please enter a city and state'
            return
        
        # Step 1: Call API to get key code for the city
        api_key = "Insert API Key Here"
        location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
        params = {
            "apikey": api_key,
            "q": city_state
        }
        response = requests.get(location_url, params=params)
        location_data = response.json()
        
        if not location_data:
            self.weather_label.text = 'City not found'
            return
        
        city_key = location_data[0]['Key']
        
        # Step 2: Use key code to fetch weather data
        weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{city_key}"
        params = {
            "apikey": api_key
        }
        response = requests.get(weather_url, params=params)
        weather_data = response.json()
        
        if not weather_data:
            self.weather_label.text = 'Weather data not available'
            return
        
        weather_text = weather_data[0]['WeatherText']
        temperature = weather_data[0]['Temperature']['Metric']['Value']
        self.weather_label.text = f'Weather: {weather_text}\nTemperature: {temperature}°C'

if __name__ == '__main__':
    WeatherApp().run()
