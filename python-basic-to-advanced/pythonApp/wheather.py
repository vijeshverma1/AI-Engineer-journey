# import tkinter as tk
# from tkinter import messagebox
# import requests

# # --- CONFIGURATION ---
# API_KEY ="bb534387d68fa1f69b46fa2136e7dc6b"  
# BASE_URL ="https://api.openweathermap.org/data/2.5/weather"

# def get_weather():
#     city = city_entry.get().strip()
#     if not city:
#         messagebox.showwarning("Warning", "Please enter a city name.")
#         return

#     # Request parameters (using metric units for Celsius)
#     params = {
#         'q': city,
#         'appid': API_KEY,
#         'units': 'metric'
#     }

#     try:
#         response = requests.get(BASE_URL, params=params)
        
#         # टर्मिनल में स्टेटस देखने के लिए
#         print(f"Status Code: {response.status_code}") 
        
#         if response.status_code == 200:
#             data = response.json()
            
#             # JSON पेलोड से डेटा निकालना
#             city_name = data['name']
#             country = data['sys']['country']
#             temp = data['main']['temp']
#             feels_like = data['main']['feels_like']
#             humidity = data['main']['humidity']
#             description = data['weather'][0]['description'].title()
#             wind_speed = data['wind']['speed']

#             # GUI लेबल्स को अपडेट करना
#             location_label.config(text=f"{city_name}, {country}")
#             temp_label.config(text=f"{round(temp)}°C")
#             desc_label.config(text=description)
            
#             stats_text = f"Feels Like: {round(feels_like)}°C  |  Humidity: {humidity}%  |  Wind: {wind_speed} m/s"
#             stats_label.config(text=stats_text)
#         else:
#             # अगर कोई एरर आती है (जैसे गलत शहर का नाम डालना या इनएक्टिव API Key)
#             data = response.json()
#             messagebox.showerror("Error", data.get("message", "Something went wrong.").capitalize())
            
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Network Issue: {e}")

# # --- GUI SETUP ---
# root = tk.Tk()
# root.title("Weather App")
# root.geometry("400x350")
# root.configure(bg="#212121")
# root.resizable(False, False)

# # Fonts
# FONT_TITLE = ("Helvetica", 14, "bold")
# FONT_TEMP = ("Helvetica", 40, "bold")
# FONT_TEXT = ("Helvetica", 12)

# # Input Section
# input_frame = tk.Frame(root, bg="#212121", pady=20)
# input_frame.pack()

# city_entry = tk.Entry(input_frame, font=FONT_TEXT, width=20, bg="#333333", fg="white", insertbackground="white", bd=0, justify="center")
# city_entry.pack(side=tk.LEFT, ipady=5, padx=5)
# city_entry.focus()
# city_entry.bind("<Return>", lambda event: get_weather()) 

# search_btn = tk.Button(input_frame, text="Search", font=FONT_TEXT, bg="#00adb5", fg="white", activebackground="#007a80", activeforeground="white", bd=0, cursor="hand2", command=get_weather)
# search_btn.pack(side=tk.LEFT, padx=5, ipady=3)

# # Output Displays
# location_label = tk.Label(root, text="Search a city to begin", font=FONT_TITLE, bg="#212121", fg="#00adb5")
# location_label.pack(pady=10)

# temp_label = tk.Label(root, text="", font=FONT_TEMP, bg="#212121", fg="white")
# temp_label.pack()

# desc_label = tk.Label(root, text="", font=FONT_TEXT, bg="#212121", fg="#b0bec5")
# desc_label.pack(pady=5)

# stats_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#212121", fg="#78909c")
# stats_label.pack(side=tk.BOTTOM, pady=30)

# root.mainloop()


# import requests

# API_KEY = "bb534387d68fa1f69b46fa2136e7dc6b"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# def get_weather(city):
#     params = {
#         'q': city,
#         'appid': API_KEY,
#         'units': 'metric'
#     }

#     # try:
#     response = requests.get(BASE_URL, params=params, timeout=10)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)

    #         print(f"City       : {data['name']}, {data['sys']['country']}")
    #         print(f"Temperature: {round(data['main']['temp'])}°C")
    #         print(f"Feels Like : {round(data['main']['feels_like'])}°C")
    #         print(f"Humidity   : {data['main']['humidity']}%")
    #         print(f"Condition  : {data['weather'][0]['description'].title()}")
    #         print(f"Wind Speed : {data['wind']['speed']} m/s")
    #     else:
    #         data = response.json()
    #         print("Error:", data.get("message", "Something went wrong."))

    # except requests.exceptions.RequestException as e:
    #     print("Network Issue:", e)

# city = input("Enter city name: ").strip()
# if city:
#     get_weather(city)
# else:
#     print("Please enter a city name.")


# import requests

# response = requests.get("https://api.openweathermap.org/data/2.5/weather")
# print(response.text)

# city = "jhunjhunu"
# url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=bb534387d68fa1f69b46fa2136e7dc6b"
# response = requests.get(url)
# data=response.json()
# print(data)


# from pyowm import OWM

# owm = OWM("bb534387d68fa1f69b46fa2136e7dc6b")
# mgr = owm.weather_manager()
# city_name=input("Enter your city: ")
# obs = mgr.weather_at_place(city_name)
# w = obs.weather

# print(w.temperature('celsius')['temp'])
# print(w.detailed_status)
# print(w.humidity)
# print(w.wind()['speed'])