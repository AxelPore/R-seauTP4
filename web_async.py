import asyncio
import argparse
import sys
import aiohttp
import aiofiles

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
    file = "/tmp/web_page"
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", action="store")

    args = parser.parse_args()

    if not args.url:
        print("You should specify a valid URL with -u or --url.")
        sys.exit(1)

    url = args.url

    page = await get_content(url).text

    await write_content(page, file)

asyncio.run(main())