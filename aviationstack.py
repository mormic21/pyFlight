import json

import requests

apikey = "dffa05a5-bc06-43e5-b76f-f0242422cb2e"
flightcode = "RYR73DT"
url = "https://airlabs.co/api/v9/flights?api_key="+apikey+"&flight_icao="+flightcode
print(url)
x = requests.get(url)
js = json.loads(x.text)
print(js["response"])
start_code = js["response"][0]["dep_iata"]
print(start_code)
end_code = js["response"][0]["arr_iata"]
print(end_code)

airport_url = "https://airlabs.co/api/v9/airports?api_key="+apikey+"&iata_code="

startport = airport_url + start_code
startresp = requests.get(startport)
start_json = json.loads(startresp.text)
print(start_json["response"])

endport = airport_url + end_code
endresp = requests.get(endport)
end_json = json.loads(endresp.text)
print(end_json["response"])