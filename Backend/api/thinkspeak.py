import requests

url = 'https://api.thingspeak.com/channels/1633090/feeds/last.json?api_key=C15DPT91QNH37GY6&status=true'

response = requests.get(url).json()
temp_value = response['field1']
hum_value = response['field2']
body_temp_value = response['field3']