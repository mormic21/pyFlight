import asyncio
import json
import websockets

arr = []

async def consumer_handler(websocket: websockets.WebSocketClientProtocol) -> None:
    try:
        async for message in websocket:
            log_message(message)
    except:
        print("Error")

async def consume(url:str) -> None:
    async with websockets.connect(url) as websocket:
        await consumer_handler(websocket)

def log_message(message:str) -> None:
    js = json.loads(message)
    try:
        arr.index(js["Tail"])
    except ValueError:
        arr.append(js["Tail"])
        print("*** NEW *** --> " + str(js["Tail"]))
    print(str(js["Timestamp"]) + "; "+str(js["Tail"]) +"; "+ str(round(js["Alt"] * 0.000305, 2)) + " km; "+ str(round(js["Speed"] * 1.852, 2)) + " km/h; "+ str(js["Track"]) + "; "+ str(js["Lat"]) + "; "+ str(js["Lng"]) + "; "+ str(js["Emitter_category"]) + ";")

if __name__ == '__main__':
    print("Timestamp; Flight; Altitude; Speed; Track; Latitude; Longitude; EmitterType")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume("wss://ws.datapool.opendatahub.testingmachine.eu/flightdata/sbs-aggregated"))
    loop.run_forever()