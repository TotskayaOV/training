import asyncio
import aiohttp
from datetime import datetime


async def download_image(url):
    start_time = datetime.now()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = 'asyncio_image' + str(datetime.now().timestamp()) + '.png'
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
        end_time = datetime.now()
        print(f"Downloaded {filename} in {end_time - start_time}")
async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

def asynchrony(urls):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))

if __name__ == '__main__':
    urls = ['https://avatars.mds.yandex.net/i?id=be0194f08f8302cc7c1c55d836b3465fbb08e5f6-12645377-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=26eef3948c699b5b1000dc9e1bb2f068db1ddf4d-10995124-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=5928f2b58c6f204d0e0c3a5c41c07e136f6d2cea-12544737-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=ae55f3cacaf3431753bccf7e3a863987f45ee0f4-10807079-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=acf92da9844f00928e2390fc14cae357a52b07bf-11481522-images-thumbs&n=13'
            ]
    asynchrony(urls)