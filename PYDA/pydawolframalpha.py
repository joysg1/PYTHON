import requests
import json


def buscar_en_wolframalpha():
    
 app_id = "UV38WAJJRH"

 question = input("Pregunta: ")

 url = f"http://api.wolframalpha.com/v2/result?i={question}&appid={app_id}"

 response = requests.get(url)

 if response.status_code == 200:
    print(response.text)
 else:
    print("Error al realizar la consulta.")




if __name__ == "__main__":
  buscar_en_wolframalpha()
