#문제 페이지에 있는 API 코드 또는 해당 코드를 활용하면 됩니다.
import requests

response = requests.post("http://20.214.105.22:7860/run/predict", json={
	"data": [
		"hello world",
	]
}).json()

data = response["data"]
print(data)