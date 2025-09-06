import requests
import json
def my_print():
    print("Print Here")

def print_rates(apiKey):
    # API_KEY = "bc42e70c56780733d29e9646389ac1dd"
    API_KEY = apiKey
    BASE_URL = "https://data.fixer.io/api/latest?access_key="
    URL = BASE_URL + API_KEY
    result = requests.get(URL)
    data = json.loads(result.text)
    # print(data)
    # print(data)
    return data    

