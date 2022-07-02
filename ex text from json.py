import requests
import json
r= requests.get("https://quotes.rest/qod.json")
res =r.json()
print(json.dumps(res,indent=4))