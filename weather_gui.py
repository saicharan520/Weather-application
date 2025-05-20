import requests
import tkinter as tk
from tkinter import messagebox
from config import API_KEY

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    API_KEY = "6a771559da479535087b128c081772be"    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result_text.set(
                f"Weather in {city.title()}:\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
        else:
            result_text.set(f"Error: {data['message']}")

    except Exception as e:
        result_text.set(f"An error occurred: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()
