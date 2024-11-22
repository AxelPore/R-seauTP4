import asyncio
import argparse
import sys
import aiohttp
import aiofiles
from os import path

async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page = await response.text()
            return page

async def write_content(page, file):
    async with aiofiles.open(file, "a") as out:
        await out.write(page)
        await out.flush() 
        
async def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", action="store")

    args = parser.parse_args()

    if not args.file:
        print("You should specify a valid file with -f or --file.")
        sys.exit(1)

    urlfile = args.file
    urlfile = "/tmp/" + urlfile
    tasks = []
    with open(urlfile, 'r') as f :
        for line in f :
            tasks.append(write_content(await get_content(line.strip()), "/tmp/web_async_" + path.basename(line.strip())))
    await asyncio.gather(*tasks)



asyncio.run(main())