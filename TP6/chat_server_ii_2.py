import asyncio

async def Server(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        message = data.decode()
        print(f"Message reçue du client : {message!r} - IP client : {addr!r}")
        IP = addr[0].replace("'", "")
        writer.write(f"Hello {IP} : {addr[1]!r}".encode())

        await writer.drain()
        

async def main():
    server = await asyncio.start_server(Server, "10.1.2.17", 13337)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on  {addrs}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())