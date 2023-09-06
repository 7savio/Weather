import requests
import json
import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city:- ")
url=f"https://api.weatherapi.com/v1/current.json?key=4cef93e29f6c4755ab9194942232707&q={city}"
r=requests.get(url)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print(w)
speak.speak(f"The Current weather in {city} is {w} degrees")