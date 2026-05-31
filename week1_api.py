 
import requests

def call_api(guessname):
    url = "https://api.agify.io"
    payload = {"name": guessname}
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        data = response.json()
        name = data.get("name")
        age = data.get("age")
        count = data.get("count")
        print(f"名字：{name}")
        print(f"預測年齡：{age}")
        print(f"樣本數：{count} 筆資料")
    except requests.exceptions.RequestException as e:
        print(f"網路請求發生錯誤：{e}")

call_api("jim")