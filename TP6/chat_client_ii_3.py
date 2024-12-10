import socket
import sys
import aioconsole
import asyncio


async def asInput(r, w) :
    while True:
        lines = []
        while True:
            ZaLine = await aioconsole.ainput()
            if not ZaLine:
                    break
            lines.append(ZaLine)
        line = '\n'.join(lines)
        if line == 'exit':
            sys.exit(0)
        w.write(line.encode())
        await w.drain()


async def asRecieve(r, w) :
    while True:
        data = await r.read(1024)
        if not data:
            break
        print(f"{data.decode()}")

async def main() :
    reader, writer = await asyncio.open_connection(host="10.1.2.17", port=13337)
    tasks = [asInput(reader, writer), asRecieve(reader, writer)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

sys.exit(0)