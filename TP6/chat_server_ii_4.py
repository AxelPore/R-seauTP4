import asyncio
global CLIENTS
CLIENTS = {}


async def handle_client_msg(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')
        CLIENTS[addr] = {}
        CLIENTS[addr]['w'] = writer
        CLIENTS[addr]['r'] = reader

        if data == b'':
            break

        message = data.decode()
        for addrs in CLIENTS.keys():
            if addrs[0] != addr[0]:
                messList = message.split("\n")
                IP = addr[0].replace("'", "")
                print(messList)
                if len(messList) > 1:
                    print("more than one")
                    CLIENTS[addrs]['w'].write(f"{IP}:{addr[1]} a dit : {messList[0]}".encode())
                    await CLIENTS[addrs]["w"].drain()
                    spaces = " " * len(f'{IP}:{addr[1]}:> ')
                    for line in messList[1:]:
                        CLIENTS[addrs]['w'].write(b"\n")
                        CLIENTS[addrs]['w'].write(f"{spaces} {line}".encode())
                        await CLIENTS[addrs]["w"].drain()
                else:
                    print("only one")
                    CLIENTS[addrs]["w"].write(f"{IP}:{addr[1]} a dit : {messList[0]}".encode())
                    await CLIENTS[addrs]["w"].drain()
                CLIENTS[addrs]['w'].write(b"\n")
                await CLIENTS[addrs]["w"].drain()
                print(f"Message received from {IP}:{addr[1]!r} : {message!r}")
            else:
                print("message not sent to self")

async def main():
    server = await asyncio.start_server(handle_client_msg, '10.1.2.17', 13337)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())