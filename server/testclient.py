
import asyncio
import websockets
import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

async def test():
    async with websockets.connect("ws://localhost:8000",) as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print(response)
 
asyncio.get_event_loop().run_until_complete(test())