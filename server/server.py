import websockets
import logging
import asyncio
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()
    def __init__(self):
        self.id = 0
        self.conn = None
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def serve_forever(self):
        start_server = websockets.serve(self.handler, 'localhost', 8000,)
        self.loop.run_until_complete(start_server)
        self.loop.run_forever()

    async def register(self, ws: WebSocketServerProtocol) -> None:
        self.clients.add(ws)

        self.log_message(ws, "Connected")

    async def register(self, ws: WebSocketServerProtocol) -> None:
        self.clients.remove(ws)
        self.log_message(ws, "Disconnected")

    async def handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol, sendAll: bool) -> None:
        async for message in ws:
            await self.sendToClients(message, sendAll)
    
    async def sendToClients(self, message: str, sendAll: bool):
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    def log_message(self, ws: WebSocketServerProtocol, message: str) -> None:
        logging.info(f"{ws.remote_address}: {message}.")


if __name__ == '__main__':
    server = Server()
    server.serve_forever()
