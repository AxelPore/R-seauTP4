import asyncio

async def compteur() :
    for i in range(11):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    tasks = [ compteur(), compteur() ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
