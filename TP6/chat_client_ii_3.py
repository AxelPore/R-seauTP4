import socket
import sys
import aioconsole
import asyncio


async def Input(reader, writer) :
    while True :
        messages = []
        while True:
            message = await aioconsole.ainput("Message : ")
            messages.append(message)
            break
        data = '\n'.join(messages)
        writer.write(data.encode())
        await writer.drain()
        await Recieve(reader, writer)
        


async def Recieve(reader, writer) :
    while True:
        data = await reader.read(1024)
        print(f"Message du serveur : {data.decode()}")
        if not data:
            break

async def main() :
    reader, writer = await asyncio.open_connection(host="10.1.2.17", port=13337)
    tasks = [Input(reader, writer), Recieve(reader, writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

sys.exit(0)