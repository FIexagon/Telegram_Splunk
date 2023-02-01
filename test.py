import json
import requests as req

requestURL = "https://api.telegram.org/bot<token>/getUpdates"
response = req.get(url=requestURL)
data = response.json()
event = data['result'][-1]
print(json.dumps(event))
