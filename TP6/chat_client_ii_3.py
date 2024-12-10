import socket
import sys
import aioconsole
import asyncio


async def Input(reader, writer) :
    while True :
        data = []
        while True:
            message = await aioconsole.ainput("Message : ")
            if not message:
                break
            data.append(message)
        writer.write(data.encode())
        await writer.drain()


async def Recieve(reader, writer) :
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(f"{data.decode()}")

async def main() :
    reader, writer = await asyncio.open_connection(host="10.1.2.17", port=13337)
    tasks = [Input(reader, writer), Recieve(reader, writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

sys.exit(0)