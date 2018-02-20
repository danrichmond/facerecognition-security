
import requests

# put your keys in the header
headers = {
    "app_id": "YOURAPPID",
    "app_key": "YOURAPPKEY"
}

payload = '{"image":"URLTOSOMEIMAGE"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content
