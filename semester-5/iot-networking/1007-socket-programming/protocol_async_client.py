import asyncio

from structure import Structure


class AsyncSocketClient:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.reader: asyncio.StreamReader
        self.writer: asyncio.StreamWriter

    async def connect(self) -> None:
        """Establishes connection to the server."""
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        print(f'Connected to {self.host}:{self.port}')

    async def send_structure(self, message: Structure) -> None:
        """Sends a message to the server."""
        print(f'Sending: {message}')
        self.writer.write(message.serialize())
        self.writer.write_eof()
        await self.writer.drain()

    async def receive_message(self) -> Structure:
        """Receives a message from the server."""
        data = await self.reader.read(-1)
        return Structure.deserialize(data)

    async def close(self) -> None:
        """Closes the connection."""
        print('Closing the connection')
        self.writer.close()
        await self.writer.wait_closed()

async def run_client(host: str, port: int) -> None:
    client = AsyncSocketClient(host, port)

    await client.connect()
    await client.send_structure(
        Structure(
            command=0x1A,
            sequence=0x00,
    ))

    # Await response from server
    response = await client.receive_message()
    print(f'Received: {response}')

    print(f'Temperature: {response.get_full_temperature()}')

    await client.close()

if __name__ == "__main__":
    host, port = "127.0.0.1", 1145  # Replace with server's IP and port
    asyncio.run(run_client(host, port))
