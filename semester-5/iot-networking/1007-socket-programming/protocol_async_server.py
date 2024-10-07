import asyncio
import os

from structure import Structure


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    while True:
        request = await reader.read()
        print(f"Received: {request}")

        if request == b'':
            print("Connection closed")
            break

        try:
            deserialized = Structure.deserialize(request)
            response = Structure(
                command=deserialized.command,
                sequence=deserialized.sequence+1,
                reserved=0x00,
                temperature=30,
                temperature_p=5,
            )
        except ValueError as e:
            print(f"Invalid request: {e}")

            response: Structure = Structure.invalid(
                command=0x1B,
                sequence=0x01
            )

        writer.write(response.serialize())
        writer.write_eof()
        await writer.drain()


async def run_server():
    host = os.environ.get("HOSTNAME", "0.0.0.0")
    port = int(os.environ.get("PORT", 1145))

    server = await asyncio.start_server(handle_client, host=host, port=port)
    async with server:
        print("listening")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(run_server())
