import requests
from jsonpath import jsonpath
import json

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
response = requests.get(url, headers=headers)
dict_data = json.loads(response.content)
data = jsonpath(dict_data, "$..A..name")
print(data)