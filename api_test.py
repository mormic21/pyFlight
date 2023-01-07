import requests
import asyncio
import time
from websockets import connect
import json

def mobility():
    url = "https://mobility.api.opendatahub.com/v2/flat%2Cnode/MeteoStation?limit=-1&offset=0&shownull=false&distinct=true"
    x = requests.get(url)
    js = x.json()
    for ob in js["data"]:
        print(ob["scode"] + "; "+ ob["sname"])
    #print(x.text)

def mobilityStationsDatatypeMeasurements():
    url = "https://mobility.api.opendatahub.com/v2/flat,node/MeteoStation/*/latest"
    x = requests.get(url)
    print(x.text)

def tourism():
    url = 'https://tourism.opendatahub.bz.it/v1/Weather/Measuringpoint?removenullvalues=false'
    x = requests.get(url)
    js = x.json()
    #print(js[0]["Temperature"])
    for ob in js:
        try:
            print(ob["Id"]+ "; " + ob["Shortname"] + "; " + ob["LocationInfo"]["TvInfo"]["Name"]["cs"] + "; " + ob["Temperature"])
        except:
            pass

def flightData():
    url = "https://api.datapool.opendatahub.testingmachine.eu/flightdata-scheduled"
    x = requests.get(url)
    js = x.json()
    #print(js)
    for ob in js:
        print(ob)

async def hello(uri):
    async with connect(uri) as websocket:
        while True:
            resp = await websocket.recv()
            msg = json.loads(resp)
            #print(type(msg["Tail"]))
            print(str(msg["Tail"]) +"; "+ str(msg["Alt"]) + "; "+ str(msg["Speed"]) + "; "+ str(msg["Lat"]) + "; "+ str(msg["Lng"]) + "; "+ str(msg["Emitter_category"]) + "; "+ str(msg["Timestamp"]) + "; ")
            time.sleep(1)


def flightDataTest():
    url = "https://api.datapool.opendatahub.testingmachine.eu/flightdata-scheduled/sbs-aggregated"
    x = requests.get(url)
    js = x.json()
    #print(js)
    for ob in js:
        print(ob)


if __name__ == '__main__':
    #tourism()
    #mobility()
    #mobilityStationsDatatypeMeasurements()
    #flightData()
    #flightDataTest()
    asyncio.run(hello("wss://ws.datapool.opendatahub.testingmachine.eu/flightdata/sbs-aggregated"))