import requests
import json

app_id = "UV38WAJJRH"

question = input("Pregunta: ")

url = f"http://api.wolframalpha.com/v2/result?i={question}&appid={app_id}"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Error al realizar la consulta.")
