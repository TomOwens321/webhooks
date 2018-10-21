import json
import requests

payload = {
    "value1":"BLUE",
    "value2":"134",
    "value3":"Betsy"
}

url = 'https://maker.ifttt.com/trigger/test-event/with/key/dYN5NG9t3p1UF9PDfvHu3Y'

response = requests.post(url, data=payload)